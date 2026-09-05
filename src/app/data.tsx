import React,{useState} from "react";
import {ScrollView,StyleSheet,Text,TouchableOpacity,View} from "react-native";

export default function Data(){
 const [snapshot,setSnapshot]=useState("SNAP-0001");
 const [exported,setExported]=useState(false);
 return <ScrollView style={s.page} contentContainerStyle={s.content}>
  <Text style={s.kicker}>LUSHKA DATA</Text><Text style={s.title}>Delta Export</Text>
  <Text style={s.sub}>Export only new or changed information since the selected snapshot.</Text>
  <View style={s.card}><Text style={s.label}>Snapshot</Text><Text style={s.value}>{snapshot}</Text><Text style={s.muted}>Formats: JSON · CSV · Markdown · PDF</Text></View>
  <TouchableOpacity style={s.button} onPress={()=>{setExported(true);setSnapshot("SNAP-"+String(Date.now()).slice(-6))}}><Text style={s.buttonText}>EXPORT NEW INFORMATION</Text></TouchableOpacity>
  {exported&&<Text style={s.success}>Delta export prepared. Connect a production storage/export service to create the actual file.</Text>}
 </ScrollView>
}
const s=StyleSheet.create({page:{flex:1,backgroundColor:"#090909"},content:{padding:22},kicker:{color:"#aaa",fontSize:11,letterSpacing:2},title:{color:"#f1eee6",fontSize:32,fontWeight:"800",marginTop:6},sub:{color:"#999",lineHeight:20,marginVertical:14},card:{backgroundColor:"#151515",borderRadius:17,padding:18,borderWidth:1,borderColor:"#292929"},label:{color:"#888"},value:{color:"#eee",fontSize:20,fontWeight:"800",marginVertical:8},muted:{color:"#999"},button:{backgroundColor:"#d6bd75",padding:16,borderRadius:13,alignItems:"center",marginTop:15},buttonText:{color:"#111",fontWeight:"900"},success:{color:"#d6bd75",marginTop:18,lineHeight:20}})
