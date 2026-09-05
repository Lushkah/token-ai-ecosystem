import React, { useState } from "react";
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from "react-native";

export default function MiningScreen() {
  const [checked, setChecked] = useState(false);

  return (
    <ScrollView style={styles.page} contentContainerStyle={styles.content}>
      <Text style={styles.kicker}>LUSHKA INFRASTRUCTURE</Text>
      <Text style={styles.title}>Mining Control</Text>
      <Text style={styles.sub}>
        Monitor authorized GPU mining workers without placing mining software
        inside the mobile wallet.
      </Text>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Intel Arc Runtime</Text>
        <Text style={styles.muted}>
          Supplied OpenCL + Level Zero installer is integrated under
          mining/intel-arc.
        </Text>
        <View style={styles.row}>
          <Text style={styles.label}>Worker status</Text>
          <Text style={styles.gold}>{checked ? "READY FOR BACKEND" : "NOT CONNECTED"}</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>GPU backend</Text>
          <Text style={styles.value}>Level Zero / OpenCL fallback</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>Authorization</Text>
          <Text style={styles.gold}>OWNER / AUTHORIZED ONLY</Text>
        </View>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Worker telemetry</Text>
        <Text style={styles.metric}>—</Text>
        <Text style={styles.muted}>
          Backend connection will populate hashrate, uptime, power, BTC mined,
          pool fees, temperature, and profitability.
        </Text>
      </View>

      <TouchableOpacity style={styles.button} onPress={() => setChecked(true)}>
        <Text style={styles.buttonText}>RUN WORKER READINESS CHECK</Text>
      </TouchableOpacity>

      <Text style={styles.note}>
        Defensive boundary: Lushka does not silently mine on phones,
        third-party servers, or devices without explicit authorization.
      </Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  page: { flex: 1, backgroundColor: "#090909" },
  content: { padding: 22, paddingBottom: 48 },
  kicker: { color: "#aaa", fontSize: 11, letterSpacing: 2, marginBottom: 8 },
  title: { color: "#f1eee6", fontSize: 32, fontWeight: "800" },
  sub: { color: "#aaa", fontSize: 14, lineHeight: 21, marginTop: 8, marginBottom: 20 },
  card: { backgroundColor: "#151515", borderRadius: 18, padding: 18, marginBottom: 14, borderWidth: 1, borderColor: "#2b2b2b" },
  cardTitle: { color: "#f1eee6", fontSize: 18, fontWeight: "700", marginBottom: 10 },
  muted: { color: "#999", lineHeight: 20 },
  row: { flexDirection: "row", justifyContent: "space-between", gap: 12, paddingTop: 13 },
  label: { color: "#aaa", flex: 1 },
  value: { color: "#ddd", flex: 1, textAlign: "right" },
  gold: { color: "#d6bd75", fontWeight: "700", textAlign: "right", flex: 1 },
  metric: { color: "#eee", fontSize: 30, fontWeight: "800", marginBottom: 4 },
  button: { backgroundColor: "#d6bd75", padding: 16, borderRadius: 14, alignItems: "center", marginTop: 4 },
  buttonText: { color: "#111", fontWeight: "800", letterSpacing: 0.5 },
  note: { color: "#777", fontSize: 12, lineHeight: 18, marginTop: 18, textAlign: "center" },
});
