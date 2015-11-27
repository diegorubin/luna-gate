package br.com.labluna.lunagate.users;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping("/users")
public class UserController {
	
	@RequestMapping(value = {"/new"}, method = RequestMethod.GET)
	public String showUserForm(Model model) {
		return "users/form";
	}

}
