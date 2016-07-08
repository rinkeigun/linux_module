# script file name No11_ATDT.gdb
# ファイルの取り込み
# (gdb) source No11_ATDT.gdb
# スクリプトの実行
# (gdb) print_db

define print_hk_result
	printf "valids=%#x, values=%#x\n", $arg0->valids, $arg0->values
end
define print_CAL_check_status
	printf "data_valid=%d, new_status=%d\n", $arg0->data_valid, $arg0->new_status
end

define print_db
	#$output_file = "~/ut/result/"
	shell date > ~/ut/result/No11_ATDT.txt
	set logging file ~/ut/result/No11_ATDT.txt
	set logging on
	set pagination 0
	set confirm off
	d

	set var $cnt = 0 
	set var $set_flg = 0

	set var $linenum = 166
	#CAL_ATDT_proc_1.c:
	break CAL_ATDT_proc_1.c:$linenum
	commands
		silent
		printf "\n=========共通部分===================\n"
		print_hk_result edit->sensor.hk
		printf "wk="
		print wk
		printf "now= %d\t", now
		printf "\n=========共通部分ここまで===========\n"
		printf "\nbreakpoint  CAL_ATDT_proc_1.c:166\n"
		printf "■5 冷却ファン異常\n"
#		printf "DATA_BIT_CLR = 2, "
#		printf "DATA_BIT_SET = 3, "  
#		printf "W_HK_COOLER_MAY_BAD = 17, "  
#		printf "R_HK_COOLER_MAY_BAD = 22, "  
		printf "A_HK_COOLER_MAY_BAD = 11, "  
#		printf "A_HK_HEATER_MAY_BAD = 10, "  
#		printf "R_HK_COOLER_RUN = 26, "  
		printf "A_HK_COLLER_RUN = 16, \n"  
		printf "wk.value.dtype= %d\n", wk.value.dtype
#160     if (data->data_valid != DATA_VALID_INVALID &&
#161         (data->new_status == NEW_STS_NORMAL ||
#162          data->new_status == NEW_STS_MAINT))
		print_CAL_check_status edit->sensor.AT
#		set var $set_bit = (unsigned long )1<< 16
#		print $set_bit = ~ $set_bit 
		

		printf "③17ビット目のビット状況を確認：%s, ", (edit->sensor.hk.valids & (1<<16) ) ? "ON" : "OFF" 
		printf "③11ビット目のビット状況を確認：%s\n", (edit->sensor.hk.values & (1<<11) ) ? "ON" : "OFF" 
#		printf "③BIT消去：%s\n", (edit->sensor.hk.valids & ($set_bit) &(1<<16) ) ? "ON" : "OFF" 
		x/4bt &edit->sensor.hk.valids 
		x/4bt &edit->sensor.hk.values 
		printf "④気温のチェック:edit->sensor.AT.value.dtype=%d >=? ", edit->sensor.AT.value.dtype
		printf "param.hkp.cooler_upper_limit_at= %d\n" , param.hkp.cooler_upper_limit_at	
#set var edit->sensor.AT.data_valid = 1
#set var edit->sensor.AT.new_status = 'N' 
		cont
	end

	set var $linenum = 170
	#CAL_ATDT_proc_1.c:
	break CAL_ATDT_proc_1.c:$linenum
	commands
		silent
		printf "\nbreakpoint CAL_lasting_check CAL_ATDT_proc_1.c:170\n"
		printf "\nケース1\n"
		printf "⑤HK16=0, 気温30以上の経過時間(%d) >= 閾値(%d) \n", now - calc->last_cooler.sample_time, param->hkp.cooler_chek_time * 60
		#p now - calc->last_cooler.sample_time 
		#p param->hkp.cooler_chek_time * 60

		if (now - calc->last_cooler.sample_time) >= (param->hkp.cooler_chek_time * 60)
			printf "edit->sensor.hk.valids = %#x ", edit->sensor.hk.valids
#set var edit->sensor.hk.valids = 1<<16 | 1<<11 | 1<<9 | 1<<2 |1<<1 | 1<<0
#set var edit->sensor.hk.values -= 1<<16
#set var edit->sensor.hk.valids |= 1<<15 
#			printf "edit->sensor.hk.valids = %#x \n", edit->sensor.hk.valids
			print "set_flgをセットしますか"
			if (1)
			#if ($set_flg != 0)
	       	 set var $set_bit = ~(unsigned long )1<< 16
#        set var $set_bit = ~ $set_bit
   		   	 #set var edit->sensor.hk.valids &= (($set_bit)&(1<<16) )
#   		   	 set var edit->sensor.hk.valids &= $set_bit 
#        	 printf "③BIT消去：%s\n", (edit->sensor.hk.valids & (1<<16)) ? "ON" : "OFF"
			x/4bt &edit->sensor.hk.values 
   		   	 set var edit->sensor.hk.values &= $set_bit 
        	 printf "③2BIT消去：%s\n", (edit->sensor.hk.values & (1<<16)) ? "ON" : "OFF"
			x/4bt &edit->sensor.hk.valids 
			x/4bt &edit->sensor.hk.values 

			end
		end

#175     if (data->value.dtype == last->value)
#176     {
#177         wk = difftime(now, last->sample_time);
#178         if (wk >= param * 60)
		printf "wk->value.dtype=%d == calc->last_cooler.value =%d\n", wk->value.dtype, calc->last_cooler.value
		printf "difftime calc->last_cooler.sample_time =%d, now = %d\n", calc->last_cooler.sample_time, now
		printf "param = %d\n", param->hkp.cooler_chek_time
		#print param
		cont
	end

	set var $linenum = 174
	#CAL_ATDT_proc_1.c:
	break CAL_ATDT_proc_1.c:$linenum
	commands
		silent
		printf "\nbreakpoint  CAL_ATDT_proc_1.c:174\n"
		printf "\nケース2\n"
		cont
	end

	break BITS_get_value
	commands
		silent
		#printf "BITS_get_value->"
		cont
	end

	#set var $linenum = 174
	#CA_s_reader_common.c:
	break CA_s_atdt_set_hk_status
	commands
		silent
		printf "\nbreakpoint  CA_s_atdt_set_hk_status\n"
		cont
	end

	#set var $linenum = 174
	#CA_s_reader_common.c:
	break CA_s_atdt_set_hk_bit_2
	commands
		silent
		printf "\nbreakpoint  CA_s_atdt_set_hk_bit_2\n"
		cont
	end


#	set var $linenum = 206
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_lasting_check  CAL_ATDT_proc_1.c:206\n"
#		printf "\nケース3\n"
#		cont
#	end
#
#	set var $linenum = 211
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_lasting_check  CAL_ATDT_proc_1.c:203\n"
#		printf "\n■6 REDL異常 2014.02.13追加\n"
#		cont
#	end
#
#	set var $linenum = 212
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_lasting_check  CAL_ATDT_proc_1.c:203\n"
#		printf "\nケース4\n"
#		cont
#	end
#
#	set var $linenum = 218
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_ATDT_proc_1.c:218\n"
#		printf "\nケース5\n"
#		cont
#	end
#
#
#	set var $linenum = 221
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  BITS_set_value  CAL_ATDT_proc_1.c:221\n"
#		printf "\nケース6\n"
#		cont
#	end
#
#
#	set var $linenum = 226
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint CAL_ATDT_proc_1.c:226\n"
#		printf "\n■7 RCLL異常 2014.02.13追加\n"
#		cont
#	end
#
#	set var $linenum = 227
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_lasting_check  CAL_ATDT_proc_1.c:227\n"
#		printf "\nケース7\n"
#		cont
#	end
#
#	set var $linenum = 233
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_ATDT_proc_1.c:233\n"
#		printf "\nケース8\n"
#		cont
#	end
#
#	set var $linenum = 236
#	#CAL_ATDT_proc_1.c:
#	break CAL_ATDT_proc_1.c:$linenum
#	commands
#		silent
#		printf "\nbreakpoint  CAL_ATDT_proc_1.c:236\n"
#		printf "\nケース9\n"
#		cont
#	end
#
	set var $linenum = 186
	#CAL_ATDT_proc_1.c:
	break CAL_ATDT_proc_1.c:$linenum
	commands
		silent
		printf "\nbreakpoint CAL_ATDT_proc_1.c:186\n"
		print "HKの結果"
		print_hk_result edit->sensor.hk 
		cont
	end


	run
end
document print_db
	usage : print_db
end
	
