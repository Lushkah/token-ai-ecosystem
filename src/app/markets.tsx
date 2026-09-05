import React, { useState } from "react";
import { ScrollView, StyleSheet, Text, TextInput, TouchableOpacity, View } from "react-native";
import { searchDexPairs, DexPair } from "../lib/dexscreener";

export default function MarketsScreen() {
  const [query, setQuery] = useState("ETH/USDC");
  const [pairs, setPairs] = useState<DexPair[]>([]);
  const [error, setError] = useState("");

  async function scan() {
    try {
      setError("");
      setPairs(await searchDexPairs(query));
    } catch (e: any) {
      setError(e?.message ?? "Market scan failed");
    }
  }

  return (
    <ScrollView style={styles.page} contentContainerStyle={styles.content}>
      <Text style={styles.kicker}>LUSHKA MARKET INTELLIGENCE</Text>
      <Text style={styles.title}>DEX Scanner</Text>
      <Text style={styles.sub}>Live pair discovery and liquidity/volume data for the AI Command Center.</Text>
      <View style={styles.searchRow}>
        <TextInput value={query} onChangeText={setQuery} style={styles.input} placeholder="ETH/USDC" placeholderTextColor="#777" />
        <TouchableOpacity style={styles.button} onPress={scan}><Text style={styles.buttonText}>SCAN</Text></TouchableOpacity>
      </View>
      {error ? <Text style={styles.error}>{error}</Text> : null}
      {pairs.slice(0, 20).map((p, i) => (
        <View style={styles.card} key={`${p.chainId}-${p.pairAddress}-${i}`}>
          <View style={styles.row}><Text style={styles.name}>{p.baseToken?.symbol ?? "?"}/{p.quoteToken?.symbol ?? "?"}</Text><Text style={styles.chain}>{p.chainId ?? "?"} · {p.dexId ?? "DEX"}</Text></View>
          <View style={styles.row}><Text style={styles.muted}>Price</Text><Text style={styles.value}>{p.priceUsd ? `$${Number(p.priceUsd).toLocaleString()}` : "—"}</Text></View>
          <View style={styles.row}><Text style={styles.muted}>24h volume</Text><Text style={styles.value}>{p.volume?.h24 != null ? `$${Number(p.volume.h24).toLocaleString()}` : "—"}</Text></View>
          <View style={styles.row}><Text style={styles.muted}>Liquidity</Text><Text style={styles.value}>{p.liquidity?.usd != null ? `$${Number(p.liquidity.usd).toLocaleString()}` : "—"}</Text></View>
        </View>
      ))}
    </ScrollView>
  );
}
const styles=StyleSheet.create({
 page:{flex:1,backgroundColor:"#090909"},content:{padding:22,paddingBottom:50},
 kicker:{color:"#aaa",fontSize:11,letterSpacing:2},title:{color:"#f1eee6",fontSize:32,fontWeight:"800",marginTop:6},
 sub:{color:"#999",lineHeight:20,marginVertical:14},searchRow:{flexDirection:"row",gap:8,marginBottom:14},
 input:{flex:1,borderWidth:1,borderColor:"#333",borderRadius:12,color:"#eee",padding:13,backgroundColor:"#151515"},
 button:{backgroundColor:"#d6bd75",borderRadius:12,paddingHorizontal:18,justifyContent:"center"},buttonText:{color:"#111",fontWeight:"800"},
 error:{color:"#df7777",marginBottom:12},card:{backgroundColor:"#151515",borderWidth:1,borderColor:"#292929",borderRadius:16,padding:15,marginBottom:10},
 row:{flexDirection:"row",justifyContent:"space-between",gap:10,paddingVertical:5},name:{color:"#eee",fontSize:17,fontWeight:"700"},chain:{color:"#888"},
 muted:{color:"#999"},value:{color:"#ddd",fontWeight:"600"}
});
