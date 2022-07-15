import 'package:flutter/material.dart';

class TelaUser extends StatefulWidget {
  const TelaUser({Key? key}) : super(key: key);

  @override
  State<TelaUser> createState() => _TelaUserState();
}

class _TelaUserState extends State<TelaUser> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.teal,
        title: const Text("User"),
      ),
      body: Container(
        padding: const EdgeInsets.only(top: 32),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(
              padding: const EdgeInsets.only(top: 32),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Image.asset("images/user.png"),
                ],
              )
            ),
            Padding(
                padding: const EdgeInsets.only(top: 32, left: 32),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: const [
                  Text(
                      "Profile",
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 32,
                      ),
                  ),
                  Text("Name: Miguel Vitor MACEDO DANTAS"),
                  Text("Age: 22"),
                  Text("Sex: Male"),
                ],
              ),
            ),
            Padding(
                padding: const EdgeInsets.only(top: 32, left: 32),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: const [
                  Text(
                    "Adress",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 32,
                    ),
                  ),
                  Text("Country: Brazil"),
                  Text("State: Rio Grande do Norte"),
                  Text("City: Natal"),
                  Text("ZIP: 59020-145"),
                  Text("Street: Av. Hermes da Fonseca, 970"),
                  Text("Complement: ap. 1201"),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 128, right: 32),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Image.asset("images/edit.png")
                ],
              ),
            )
          ],
        ),
      )
    );
  }
}
