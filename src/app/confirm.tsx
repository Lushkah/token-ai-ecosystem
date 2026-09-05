import React from "react";
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { evaluateTrade } from "../lib/policy";
import { useLocalSearchParams, router } from "expo-router";

export default function ConfirmScreen() {
  const p=useLocalSearchParams<{token?:string,amount?:string,slippage?:string}>();
  const amount=Number(p.amount??"0"), slippage=Number(p.slippage??"50");
  const risk=evaluateTrade({side:"buy",token:p.token??"UNKNOWN",amountUsd:amount,slippageBps:slippage});
  return <ScrollView style={s.page} contentContainerStyle={s.content}>
    <Text style={s.kicker}>SECURITY GATE</Text><Text style={s.title}>Review Action</Text>
    <View style={s.card}>
      <Text style={s.line}>Asset <Text style={s.val}>{p.token??"UNKNOWN"}</Text></Text>
      <Text style={s.line}>Amount <Text style={s.val}>${amount.toLocaleString()}</Text></Text>
      <Text style={s.line}>Slippage <Text style={s.val}>{(slippage/100).toFixed(2)}%</Text></Text>
      <Text style={s.line}>Risk <Text style={risk.level==="LOW"?s.good:s.warn}>{risk.level}</Text></Text>
      {risk.reasons.map(x=><Text key={x} style={s.reason}>• {x}</Text>)}
    </View>
    <Text style={s.note}>No transaction is signed from this screen. The wallet must explicitly authorize the final action.</Text>
    <TouchableOpacity style={s.button} onPress={()=>router.back()}><Text style={s.buttonText}>BACK TO WALLET</Text></TouchableOpacity>
  </ScrollView>
}
const s=StyleSheet.create({page:{flex:1,backgroundColor:"#090909"},content:{padding:22},kicker:{color:"#aaa",fontSize:11,letterSpacing:2},title:{color:"#f1eee6",fontSize:31,fontWeight:"800",marginTop:6,marginBottom:20},card:{backgroundColor:"#151515",borderRadius:18,borderWidth:1,borderColor:"#292929",padding:18},line:{color:"#aaa",paddingVertical:9},val:{color:"#eee",fontWeight:"700"},good:{color:"#d6bd75",fontWeight:"800"},warn:{color:"#e58b70",fontWeight:"800"},reason:{color:"#bbb",paddingTop:8},note:{color:"#777",lineHeight:19,marginVertical:20},button:{backgroundColor:"#d6bd75",padding:16,borderRadius:13,alignItems:"center"},buttonText:{color:"#111",fontWeight:"800"}})
