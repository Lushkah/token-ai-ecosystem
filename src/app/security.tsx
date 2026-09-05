import React,{useState} from "react";
import {ScrollView,StyleSheet,Text,TouchableOpacity,View} from "react-native";

export default function Security(){
 const [frozen,setFrozen]=useState(false); const [scan,setScan]=useState(false);
 const checks=["Wallet key isolation","Transaction preview","Phishing/domain check","Token/contract risk","AI permissions","Approval/spending limits","Anomaly monitoring"];
 return <ScrollView style={s.page} contentContainerStyle={s.content}>
  <Text style={s.kicker}>LUSHKA SECURITY CENTER</Text><Text style={s.title}>Protection</Text>
  <View style={s.banner}><Text style={s.bannerTitle}>{frozen?"EMERGENCY MODE ACTIVE":"DEFENSIVE MODE"}</Text><Text style={s.muted}>AI can detect and explain risk; it cannot bypass wallet authorization.</Text></View>
  {checks.map(x=><View style={s.check} key={x}><Text style={s.dot}>●</Text><Text style={s.ct}>{x}</Text><Text style={s.ok}>{scan?"CHECKED":"READY"}</Text></View>)}
  <TouchableOpacity style={s.button} onPress={()=>setScan(true)}><Text style={s.buttonText}>RUN SECURITY CHECK</Text></TouchableOpacity>
  <TouchableOpacity style={s.freeze} onPress={()=>setFrozen(!frozen)}><Text style={s.freezeText}>{frozen?"DISABLE EMERGENCY MODE":"EMERGENCY FREEZE"}</Text></TouchableOpacity>
  <Text style={s.note}>Emergency controls should be connected to an audited backend/multisig policy before handling production treasury funds.</Text>
 </ScrollView>
}
const s=StyleSheet.create({page:{flex:1,backgroundColor:"#090909"},content:{padding:22,paddingBottom:50},kicker:{color:"#aaa",fontSize:11,letterSpacing:2},title:{color:"#f1eee6",fontSize:32,fontWeight:"800",marginTop:6,marginBottom:18},banner:{backgroundColor:"#151515",borderRadius:18,borderWidth:1,borderColor:"#3b3525",padding:17,marginBottom:14},bannerTitle:{color:"#d6bd75",fontWeight:"900",letterSpacing:1},muted:{color:"#999",lineHeight:19,marginTop:7},check:{backgroundColor:"#121212",padding:15,borderRadius:13,marginBottom:7,flexDirection:"row",alignItems:"center"},dot:{color:"#d6bd75",marginRight:9},ct:{color:"#ddd",flex:1},ok:{color:"#888",fontSize:11,fontWeight:"800"},button:{backgroundColor:"#d6bd75",padding:16,borderRadius:13,alignItems:"center",marginTop:8},buttonText:{color:"#111",fontWeight:"900"},freeze:{borderWidth:1,borderColor:"#744",padding:15,borderRadius:13,alignItems:"center",marginTop:10},freezeText:{color:"#e58b70",fontWeight:"900"},note:{color:"#666",fontSize:12,lineHeight:18,textAlign:"center",marginTop:18}})
