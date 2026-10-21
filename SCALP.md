# Range-Scalp Bot

*Updated Wed Oct 21 02:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26567 | 23137 | 3430 (33) | 6 | $-7761.05 | -4.6% |
| **+10¢** | 19990 | 16030 | 3960 (48) | 7 | $-6844.33 | -5.4% |
| **+15¢** | 16729 | 12470 | 4259 (72) | 8 | $-6091.73 | -5.8% |
| **+20¢** | 14809 | 10344 | 4465 (91) | 8 | $-5469.36 | -5.9% |
| **+10¢ (15¢ stop)** | 32554 | 32501 | 53 (30) | 0 | $-11917.76 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 02:35 | +10 stop | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-21 02:35 | +20 | ETH | UP | 0.66 | 0.87 | 1.86 |
| 10-21 02:35 | +15 | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-21 02:35 | +10 | ETH | UP | 0.66 | 0.83 | 1.44 |
| 10-21 02:35 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 10-21 02:35 | +10 stop | BTC | UP | 0.61 | 0.77 | 1.30 |
| 10-21 02:34 | +10 stop | NEAR | UP | 0.66 | 0.78 | 0.91 |
| 10-21 02:33 | +10 stop | ZEC | UP | 0.65 | 0.81 | 1.33 |
| 10-21 02:33 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.73 |
| 10-21 02:33 | +10 stop | SOL | UP | 0.67 | 0.81 | 1.13 |
| 10-21 02:33 | +10 stop | BTC | UP | 0.67 | 0.77 | 0.71 |
| 10-21 02:33 | +10 stop | BNB | UP | 0.58 | 0.72 | 1.07 |
| 10-21 02:33 | +10 | BNB | UP | 0.58 | 0.72 | 1.07 |
| 10-21 02:33 | +5 | BNB | UP | 0.58 | 0.65 | 0.36 |
| 10-21 02:33 | +10 stop | BNB | DOWN | 0.47 | 0.60 | 0.95 |
| 10-21 02:33 | +20 | BNB | DOWN | 0.47 | open |  |
| 10-21 02:33 | +15 | BNB | DOWN | 0.47 | open |  |
| 10-21 02:33 | +10 | BNB | DOWN | 0.47 | 0.60 | 0.95 |
| 10-21 02:33 | +5 | BNB | DOWN | 0.47 | 0.60 | 0.95 |
| 10-21 02:32 | +10 stop | SOL | DOWN | 0.69 | 0.46 | -2.63 |
| 10-21 02:32 | +10 | SOL | DOWN | 0.69 | open |  |
| 10-21 02:32 | +10 stop | DOGE | DOWN | 0.57 | 0.30 | -3.02 |
| 10-21 02:32 | +10 | DOGE | DOWN | 0.57 | open |  |
| 10-21 02:32 | +5 | HYPE | UP | 0.57 | 0.65 | 0.42 |
| 10-21 02:32 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-21 02:32 | +10 | BTC | DOWN | 0.60 | open |  |
| 10-21 02:32 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-21 02:32 | +5 | SOL | DOWN | 0.68 | open |  |
| 10-21 02:32 | +5 | DOGE | DOWN | 0.58 | open |  |
| 10-21 02:32 | +5 | XRP | DOWN | 0.56 | open |  |
| 10-21 02:31 | +10 stop | NEAR | DOWN | 0.65 | 0.48 | -2.04 |
| 10-21 02:31 | +20 | NEAR | DOWN | 0.65 | open |  |
| 10-21 02:31 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-21 02:31 | +10 | NEAR | DOWN | 0.65 | open |  |
| 10-21 02:31 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-21 02:31 | +10 stop | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-21 02:31 | +20 | BTC | DOWN | 0.51 | open |  |
| 10-21 02:31 | +15 | BTC | DOWN | 0.51 | open |  |
| 10-21 02:31 | +10 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
| 10-21 02:31 | +5 | BTC | DOWN | 0.51 | 0.61 | 0.65 |
