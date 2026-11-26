# Range-Scalp Bot

*Updated Thu Nov 26 22:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72979 | 63697 | 9282 (158) | 0 | $-19447.72 | -4.2% |
| **+10¢** | 54405 | 43568 | 10837 (203) | 0 | $-18046.14 | -5.3% |
| **+15¢** | 45561 | 33887 | 11674 (261) | 0 | $-16138.62 | -5.6% |
| **+20¢** | 40543 | 28252 | 12291 (327) | 0 | $-14527.21 | -5.7% |
| **+10¢ (15¢ stop)** | 88869 | 88660 | 209 (128) | 0 | $-32770.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 22:02 | +10 stop | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-26 22:02 | +20 | ZEC | DOWN | 0.67 | 0.91 | 2.22 |
| 11-26 22:02 | +15 | ZEC | DOWN | 0.67 | 0.83 | 1.34 |
| 11-26 22:02 | +10 | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-26 22:02 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-26 22:01 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-26 22:01 | +20 | NEAR | DOWN | 0.68 | 0.90 | 2.01 |
| 11-26 22:01 | +15 | NEAR | DOWN | 0.68 | 0.86 | 1.55 |
| 11-26 22:01 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-26 22:01 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-26 22:01 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-26 22:01 | +20 | DOGE | DOWN | 0.70 | 0.91 | 1.88 |
| 11-26 22:01 | +15 | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-26 22:01 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-26 22:01 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-26 22:01 | +10 stop | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-26 22:01 | +20 | HYPE | DOWN | 0.65 | 0.92 | 2.47 |
| 11-26 22:01 | +15 | HYPE | DOWN | 0.65 | 0.92 | 2.47 |
| 11-26 22:01 | +10 | HYPE | DOWN | 0.65 | 0.79 | 1.12 |
| 11-26 22:01 | +5 | HYPE | DOWN | 0.65 | 0.74 | 0.60 |
| 11-26 21:56 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-26 21:55 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-26 21:54 | +10 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-26 21:54 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-26 21:54 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 11-26 21:53 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 11-26 21:53 | +10 stop | DOGE | DOWN | 0.69 | 0.52 | -2.03 |
| 11-26 21:53 | +10 stop | BNB | UP | 0.59 | 0.43 | -1.97 |
| 11-26 21:53 | +20 | BNB | UP | 0.59 | no | -6.07 |
| 11-26 21:53 | +15 | BNB | UP | 0.59 | no | -6.07 |
| 11-26 21:53 | +10 | BNB | UP | 0.59 | no | -6.07 |
| 11-26 21:53 | +5 | BNB | UP | 0.59 | no | -6.07 |
| 11-26 21:53 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-26 21:52 | +10 stop | BTC | UP | 0.39 | 0.63 | 2.06 |
| 11-26 21:52 | +10 stop | SOL | UP | 0.55 | 0.29 | -2.93 |
| 11-26 21:52 | +20 | SOL | UP | 0.55 | no | -5.68 |
| 11-26 21:52 | +15 | SOL | UP | 0.55 | no | -5.68 |
| 11-26 21:52 | +10 | SOL | UP | 0.55 | no | -5.68 |
| 11-26 21:52 | +5 | SOL | UP | 0.55 | no | -5.68 |
| 11-26 21:52 | +10 stop | NEAR | UP | 0.65 | 0.37 | -3.13 |
