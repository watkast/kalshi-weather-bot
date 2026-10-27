# Range-Scalp Bot

*Updated Tue Oct 27 00:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35674 | 31130 | 4544 (43) | 5 | $-10010.97 | -4.5% |
| **+10¢** | 26671 | 21416 | 5255 (65) | 5 | $-8849.68 | -5.3% |
| **+15¢** | 22328 | 16678 | 5650 (89) | 4 | $-7900.09 | -5.6% |
| **+20¢** | 19793 | 13873 | 5920 (112) | 4 | $-6952.40 | -5.6% |
| **+10¢ (15¢ stop)** | 43733 | 43671 | 62 (33) | 0 | $-16664.72 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 00:32 | +10 stop | BTC | UP | 0.53 | 0.31 | -2.53 |
| 10-27 00:32 | +20 | BTC | UP | 0.53 | open |  |
| 10-27 00:32 | +15 | BTC | UP | 0.53 | open |  |
| 10-27 00:32 | +10 | BTC | UP | 0.53 | open |  |
| 10-27 00:32 | +5 | BTC | UP | 0.53 | open |  |
| 10-27 00:32 | +10 stop | HYPE | UP | 0.62 | 0.44 | -2.15 |
| 10-27 00:32 | +5 | HYPE | UP | 0.62 | open |  |
| 10-27 00:31 | +10 stop | NEAR | UP | 0.64 | 0.47 | -2.05 |
| 10-27 00:31 | +20 | NEAR | UP | 0.64 | open |  |
| 10-27 00:31 | +15 | NEAR | UP | 0.64 | open |  |
| 10-27 00:31 | +10 | NEAR | UP | 0.64 | open |  |
| 10-27 00:31 | +5 | NEAR | UP | 0.64 | open |  |
| 10-27 00:31 | +10 stop | DOGE | UP | 0.59 | 0.35 | -2.73 |
| 10-27 00:31 | +15 | DOGE | UP | 0.59 | open |  |
| 10-27 00:31 | +10 | DOGE | UP | 0.59 | open |  |
| 10-27 00:31 | +5 | DOGE | UP | 0.59 | open |  |
| 10-27 00:31 | +10 stop | SOL | UP | 0.64 | 0.35 | -3.22 |
| 10-27 00:31 | +10 | SOL | UP | 0.64 | open |  |
| 10-27 00:31 | +5 | SOL | UP | 0.64 | open |  |
| 10-27 00:31 | +10 stop | ZEC | DOWN | 0.50 | 0.66 | 1.26 |
| 10-27 00:31 | +20 | ZEC | DOWN | 0.49 | 0.72 | 1.97 |
| 10-27 00:31 | +15 | ZEC | DOWN | 0.49 | 0.66 | 1.36 |
| 10-27 00:31 | +10 | ZEC | DOWN | 0.49 | 0.66 | 1.36 |
| 10-27 00:31 | +5 | ZEC | DOWN | 0.49 | 0.58 | 0.54 |
| 10-27 00:31 | +10 stop | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 00:31 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-27 00:31 | +15 | BNB | DOWN | 0.60 | 0.75 | 1.19 |
| 10-27 00:31 | +10 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 00:31 | +5 | BNB | DOWN | 0.60 | 0.73 | 0.99 |
| 10-27 00:31 | +10 stop | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-27 00:31 | +20 | ETH | DOWN | 0.51 | 0.73 | 1.88 |
| 10-27 00:31 | +15 | ETH | DOWN | 0.51 | 0.73 | 1.88 |
| 10-27 00:31 | +10 | ETH | DOWN | 0.51 | 0.61 | 0.65 |
| 10-27 00:31 | +5 | ETH | DOWN | 0.51 | 0.57 | 0.24 |
| 10-27 00:31 | +10 stop | HYPE | DOWN | 0.45 | 0.55 | 0.64 |
| 10-27 00:31 | +20 | HYPE | DOWN | 0.47 | open |  |
| 10-27 00:31 | +15 | HYPE | DOWN | 0.47 | open |  |
| 10-27 00:31 | +10 | HYPE | DOWN | 0.47 | open |  |
| 10-27 00:31 | +5 | HYPE | DOWN | 0.48 | 0.55 | 0.34 |
| 10-27 00:31 | +10 stop | DOGE | DOWN | 0.46 | 0.61 | 1.15 |
