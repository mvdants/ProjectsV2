import 'package:flutter/material.dart';


class TelaConfig extends StatefulWidget {
  const TelaConfig({Key? key}) : super(key: key);

  @override
  State<TelaConfig> createState() => _TelaConfigState();
}

class _TelaConfigState extends State<TelaConfig> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.teal,
        title: const Text("Settings"),
      ),
      body: Container(),
    );
  }
}
