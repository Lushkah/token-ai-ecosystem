import React,{useMemo} from "react";
import {ScrollView,StyleSheet,Text,View} from "react-native";

export default function AIScreen(){
 const signals=useMemo(()=>[
  ["Market regime","MONITOR","No guaranteed-profit signal"],
  ["Liquidity","CHECK","Validate pool depth before execution"],
  ["Security","READY","Use transaction simulation and approval limits"],
  ["Execution","GATED","Policy engine required before signing"],
  ["Info Coin equation","ACTIVE","Score is informational, not a guaranteed price"]
 ],[]);
 return <ScrollView style={s.page} contentContainerStyle={s.content}>
  <Text style={s.kicker}>LUSHKA AI COMMAND CENTER</Text><Text style={s.title}>Intelligence</Text>
  <Text style={s.sub}>Continuous analysis with explainable signals and a hard authorization boundary.</Text>
  {signals.map(([a,b,c])=><View style={s.card} key={a}><View style={s.row}><Text style={s.name}>{a}</Text><Text style={s.status}>{b}</Text></View><Text style={s.muted}>{c}</Text></View>)}
  <View style={s.equation}><Text style={s.eqTitle}>INFO COIN MODEL</Text><Text style={s.eq}>V = f(Q, D, L, R, C, E)</Text><Text style={s.muted}>AI evaluates evidence quality, data contribution, liquidity, activity, complexity, and economic activity. It does not promise appreciation.</Text></View>
 </ScrollView>
}
const s=StyleSheet.create({page:{flex:1,backgroundColor:"#090909"},content:{padding:22,paddingBottom:50},kicker:{color:"#aaa",fontSize:11,letterSpacing:2},title:{color:"#f1eee6",fontSize:32,fontWeight:"800",marginTop:6},sub:{color:"#999",lineHeight:20,marginVertical:14},card:{backgroundColor:"#151515",padding:16,borderRadius:16,borderWidth:1,borderColor:"#292929",marginBottom:10},row:{flexDirection:"row",justifyContent:"space-between"},name:{color:"#eee",fontWeight:"700"},status:{color:"#d6bd75",fontWeight:"800"},muted:{color:"#999",lineHeight:19,marginTop:8},equation:{padding:18,borderRadius:18,backgroundColor:"#111",borderWidth:1,borderColor:"#403a2a",marginTop:5},eqTitle:{color:"#aaa",fontSize:11,letterSpacing:1.5},eq:{color:"#f1eee6",fontSize:22,fontWeight:"800",marginVertical:10}})
