# Range-Scalp Bot

*Updated Thu Oct 22 19:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29192 | 25417 | 3775 (39) | 5 | $-8553.07 | -4.7% |
| **+10¢** | 21898 | 17530 | 4368 (55) | 6 | $-7667.40 | -5.6% |
| **+15¢** | 18332 | 13639 | 4693 (78) | 6 | $-6859.07 | -6.0% |
| **+20¢** | 16229 | 11310 | 4919 (100) | 7 | $-6183.16 | -6.1% |
| **+10¢ (15¢ stop)** | 35838 | 35779 | 59 (32) | 0 | $-13505.14 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 19:51 | +5 | BNB | UP | 0.71 | 0.78 | 0.42 |
| 10-22 19:50 | +10 stop | XRP | UP | 0.69 | 0.79 | 0.73 |
| 10-22 19:50 | +10 stop | BNB | DOWN | 0.51 | 0.28 | -2.68 |
| 10-22 19:50 | +20 | BNB | DOWN | 0.51 | open |  |
| 10-22 19:50 | +15 | BNB | DOWN | 0.51 | open |  |
| 10-22 19:50 | +10 | BNB | DOWN | 0.51 | open |  |
| 10-22 19:50 | +5 | BNB | DOWN | 0.51 | 0.59 | 0.45 |
| 10-22 19:50 | +10 stop | ZEC | DOWN | 0.33 | 0.56 | 1.96 |
| 10-22 19:50 | +20 | ZEC | DOWN | 0.33 | 0.56 | 1.96 |
| 10-22 19:50 | +15 | ZEC | DOWN | 0.33 | 0.56 | 1.96 |
| 10-22 19:50 | +10 | ZEC | DOWN | 0.33 | 0.56 | 1.96 |
| 10-22 19:50 | +5 | ZEC | DOWN | 0.35 | 0.56 | 1.76 |
| 10-22 19:50 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
| 10-22 19:50 | +10 stop | XRP | DOWN | 0.60 | 0.39 | -2.44 |
| 10-22 19:50 | +20 | XRP | DOWN | 0.62 | open |  |
| 10-22 19:50 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-22 19:50 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-22 19:50 | +5 | XRP | DOWN | 0.63 | open |  |
| 10-22 19:50 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-22 19:48 | +10 stop | ETH | DOWN | 0.62 | 0.46 | -1.95 |
| 10-22 19:48 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-22 19:48 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-22 19:48 | +10 | ETH | DOWN | 0.62 | open |  |
| 10-22 19:48 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-22 19:48 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-22 19:48 | +10 stop | BTC | DOWN | 0.65 | 0.47 | -2.14 |
| 10-22 19:48 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-22 19:48 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-22 19:48 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-22 19:48 | +5 | BTC | DOWN | 0.65 | open |  |
| 10-22 19:48 | +10 stop | NEAR | DOWN | 0.68 | 0.41 | -3.03 |
| 10-22 19:48 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-22 19:48 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-22 19:46 | +10 stop | HYPE | DOWN | 0.64 | 0.80 | 1.27 |
| 10-22 19:46 | +20 | HYPE | DOWN | 0.64 | open |  |
| 10-22 19:46 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.27 |
| 10-22 19:46 | +10 | HYPE | DOWN | 0.63 | 0.74 | 0.75 |
| 10-22 19:46 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.44 |
| 10-22 19:46 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-22 19:46 | +20 | NEAR | DOWN | 0.65 | open |  |
