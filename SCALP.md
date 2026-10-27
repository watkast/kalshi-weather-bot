# Range-Scalp Bot

*Updated Tue Oct 27 08:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36274 | 31676 | 4598 (43) | 3 | $-10015.48 | -4.4% |
| **+10¢** | 27116 | 21798 | 5318 (65) | 6 | $-8839.83 | -5.2% |
| **+15¢** | 22689 | 16978 | 5711 (89) | 5 | $-7795.13 | -5.5% |
| **+20¢** | 20107 | 14123 | 5984 (112) | 4 | $-6831.08 | -5.4% |
| **+10¢ (15¢ stop)** | 44490 | 44427 | 63 (33) | 0 | $-16965.38 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 08:42 | +10 stop | DOGE | DOWN | 0.57 | 0.27 | -3.28 |
| 10-27 08:42 | +15 | DOGE | DOWN | 0.57 | open |  |
| 10-27 08:42 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-27 08:42 | +5 | DOGE | DOWN | 0.57 | 0.62 | 0.19 |
| 10-27 08:41 | +5 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-27 08:41 | +10 stop | DOGE | UP | 0.47 | 0.24 | -2.61 |
| 10-27 08:40 | +10 stop | BTC | UP | 0.49 | 0.33 | -1.94 |
| 10-27 08:40 | +20 | BTC | UP | 0.49 | open |  |
| 10-27 08:40 | +15 | BTC | UP | 0.49 | open |  |
| 10-27 08:40 | +10 | BTC | UP | 0.49 | open |  |
| 10-27 08:40 | +5 | BTC | UP | 0.49 | 0.57 | 0.44 |
| 10-27 08:40 | +10 stop | SOL | UP | 0.53 | 0.25 | -3.12 |
| 10-27 08:40 | +20 | SOL | UP | 0.54 | open |  |
| 10-27 08:40 | +15 | SOL | UP | 0.54 | open |  |
| 10-27 08:40 | +10 | SOL | UP | 0.54 | open |  |
| 10-27 08:40 | +5 | SOL | UP | 0.54 | open |  |
| 10-27 08:39 | +10 stop | NEAR | UP | 0.51 | 0.18 | -3.59 |
| 10-27 08:39 | +20 | NEAR | UP | 0.53 | open |  |
| 10-27 08:39 | +15 | NEAR | UP | 0.53 | open |  |
| 10-27 08:39 | +10 | NEAR | UP | 0.53 | open |  |
| 10-27 08:39 | +5 | NEAR | UP | 0.55 | open |  |
| 10-27 08:39 | +10 | XRP | UP | 0.70 | open |  |
| 10-27 08:39 | +10 stop | ZEC | UP | 0.71 | 0.56 | -1.83 |
| 10-27 08:39 | +15 | ZEC | UP | 0.70 | open |  |
| 10-27 08:39 | +10 | ZEC | UP | 0.70 | open |  |
| 10-27 08:39 | +5 | ZEC | UP | 0.70 | open |  |
| 10-27 08:38 | +10 stop | BTC | UP | 0.67 | 0.87 | 1.76 |
| 10-27 08:38 | +10 stop | XRP | UP | 0.55 | 0.67 | 0.86 |
| 10-27 08:38 | +10 stop | SOL | UP | 0.57 | 0.80 | 2.00 |
| 10-27 08:38 | +5 | SOL | UP | 0.57 | 0.80 | 2.00 |
| 10-27 08:38 | +10 stop | HYPE | DOWN | 0.54 | 0.37 | -2.05 |
| 10-27 08:38 | +20 | HYPE | DOWN | 0.54 | 0.83 | 2.62 |
| 10-27 08:38 | +15 | HYPE | DOWN | 0.54 | 0.83 | 2.62 |
| 10-27 08:38 | +10 | HYPE | DOWN | 0.54 | 0.83 | 2.62 |
| 10-27 08:38 | +5 | HYPE | DOWN | 0.56 | 0.63 | 0.38 |
| 10-27 08:38 | +10 stop | ETH | DOWN | 0.62 | 0.41 | -2.44 |
| 10-27 08:37 | +5 | SOL | DOWN | 0.50 | 0.65 | 1.16 |
| 10-27 08:37 | +10 stop | XRP | DOWN | 0.69 | 0.52 | -2.03 |
| 10-27 08:37 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-27 08:36 | +10 stop | SOL | DOWN | 0.67 | 0.49 | -2.14 |
