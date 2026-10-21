# Range-Scalp Bot

*Updated Wed Oct 21 11:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27159 | 23651 | 3508 (39) | 7 | $-7890.20 | -4.6% |
| **+10¢** | 20422 | 16368 | 4054 (55) | 7 | $-6980.72 | -5.4% |
| **+15¢** | 17098 | 12734 | 4364 (78) | 8 | $-6254.25 | -5.8% |
| **+20¢** | 15139 | 10566 | 4573 (98) | 9 | $-5604.44 | -5.9% |
| **+10¢ (15¢ stop)** | 33325 | 33266 | 59 (32) | 0 | $-12333.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 11:53 | +10 stop | NEAR | UP | 0.59 | 0.37 | -2.54 |
| 10-21 11:51 | +10 stop | HYPE | DOWN | 0.55 | 0.27 | -3.16 |
| 10-21 11:51 | +10 stop | NEAR | DOWN | 0.53 | 0.28 | -2.83 |
| 10-21 11:50 | +10 stop | DOGE | UP | 0.64 | 0.88 | 2.15 |
| 10-21 11:49 | +10 stop | BTC | UP | 0.61 | 0.75 | 1.09 |
| 10-21 11:49 | +10 stop | HYPE | UP | 0.63 | 0.45 | -2.19 |
| 10-21 11:49 | +10 | HYPE | UP | 0.63 | 0.83 | 1.69 |
| 10-21 11:49 | +5 | HYPE | UP | 0.63 | 0.72 | 0.54 |
| 10-21 11:49 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 10-21 11:49 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.09 |
| 10-21 11:48 | +10 stop | HYPE | DOWN | 0.45 | 0.55 | 0.64 |
| 10-21 11:48 | +10 | HYPE | DOWN | 0.45 | 0.55 | 0.64 |
| 10-21 11:48 | +5 | HYPE | DOWN | 0.45 | 0.55 | 0.64 |
| 10-21 11:48 | +10 stop | ZEC | UP | 0.58 | 0.81 | 2.01 |
| 10-21 11:48 | +10 stop | SOL | UP | 0.69 | 0.83 | 1.15 |
| 10-21 11:48 | +10 stop | ETH | UP | 0.70 | 0.80 | 0.76 |
| 10-21 11:48 | +10 stop | NEAR | UP | 0.66 | 0.50 | -1.94 |
| 10-21 11:48 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-21 11:47 | +5 | BNB | DOWN | 0.64 | open |  |
| 10-21 11:47 | +5 | SOL | DOWN | 0.67 | open |  |
| 10-21 11:47 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-21 11:47 | +5 | DOGE | DOWN | 0.64 | open |  |
| 10-21 11:46 | +10 stop | ETH | DOWN | 0.70 | 0.46 | -2.73 |
| 10-21 11:46 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-21 11:46 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-21 11:46 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-21 11:46 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-21 11:46 | +10 stop | ZEC | DOWN | 0.54 | 0.38 | -1.95 |
| 10-21 11:46 | +20 | ZEC | DOWN | 0.54 | open |  |
| 10-21 11:46 | +15 | ZEC | DOWN | 0.54 | open |  |
| 10-21 11:46 | +10 | ZEC | DOWN | 0.55 | open |  |
| 10-21 11:46 | +5 | ZEC | DOWN | 0.55 | 0.60 | 0.15 |
| 10-21 11:46 | +10 stop | BTC | DOWN | 0.56 | 0.37 | -2.25 |
| 10-21 11:46 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-21 11:46 | +15 | BTC | DOWN | 0.56 | open |  |
| 10-21 11:46 | +10 | BTC | DOWN | 0.56 | open |  |
| 10-21 11:46 | +5 | BTC | DOWN | 0.56 | open |  |
| 10-21 11:46 | +10 stop | BNB | DOWN | 0.59 | 0.40 | -2.23 |
| 10-21 11:46 | +20 | BNB | DOWN | 0.59 | open |  |
| 10-21 11:46 | +15 | BNB | DOWN | 0.59 | open |  |
