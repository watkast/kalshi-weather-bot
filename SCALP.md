# Range-Scalp Bot

*Updated Tue Nov 10 16:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54744 | 47751 | 6993 (91) | 2 | $-14917.48 | -4.3% |
| **+10¢** | 40906 | 32747 | 8159 (121) | 2 | $-13835.35 | -5.4% |
| **+15¢** | 34289 | 25495 | 8794 (155) | 2 | $-12580.56 | -5.8% |
| **+20¢** | 30528 | 21300 | 9228 (204) | 3 | $-11012.76 | -5.8% |
| **+10¢ (15¢ stop)** | 66690 | 66576 | 114 (70) | 0 | $-24671.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 16:34 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.76 |
| 11-10 16:34 | +10 stop | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-10 16:33 | +10 stop | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 16:33 | +10 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-10 16:33 | +5 | HYPE | UP | 0.51 | open |  |
| 11-10 16:33 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-10 16:32 | +10 stop | BTC | DOWN | 0.51 | 0.67 | 1.26 |
| 11-10 16:32 | +10 | BTC | DOWN | 0.51 | 0.67 | 1.26 |
| 11-10 16:32 | +10 stop | SOL | DOWN | 0.54 | 0.65 | 0.76 |
| 11-10 16:32 | +10 | SOL | DOWN | 0.54 | 0.65 | 0.76 |
| 11-10 16:32 | +5 | SOL | DOWN | 0.54 | 0.65 | 0.76 |
| 11-10 16:32 | +10 stop | NEAR | DOWN | 0.51 | 0.77 | 2.29 |
| 11-10 16:32 | +10 | NEAR | DOWN | 0.51 | 0.77 | 2.29 |
| 11-10 16:32 | +5 | NEAR | DOWN | 0.51 | 0.57 | 0.24 |
| 11-10 16:32 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 11-10 16:32 | +20 | ETH | DOWN | 0.67 | open |  |
| 11-10 16:32 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-10 16:32 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 16:32 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 11-10 16:32 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-10 16:32 | +5 | XRP | DOWN | 0.62 | 0.68 | 0.28 |
| 11-10 16:32 | +10 stop | DOGE | DOWN | 0.71 | 0.52 | -2.23 |
| 11-10 16:32 | +20 | DOGE | DOWN | 0.70 | 0.90 | 1.79 |
| 11-10 16:32 | +15 | DOGE | DOWN | 0.70 | 0.86 | 1.36 |
| 11-10 16:32 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-10 16:32 | +5 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-10 16:32 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 11-10 16:32 | +20 | BNB | DOWN | 0.68 | 0.88 | 1.76 |
| 11-10 16:32 | +15 | BNB | DOWN | 0.68 | 0.87 | 1.66 |
| 11-10 16:32 | +10 | BNB | DOWN | 0.68 | 0.87 | 1.66 |
| 11-10 16:32 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-10 16:31 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-10 16:31 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-10 16:31 | +15 | BTC | DOWN | 0.57 | 0.76 | 1.59 |
| 11-10 16:31 | +10 | BTC | DOWN | 0.57 | 0.68 | 0.76 |
| 11-10 16:31 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 11-10 16:31 | +10 stop | HYPE | UP | 0.67 | 0.47 | -2.38 |
| 11-10 16:31 | +20 | HYPE | UP | 0.67 | open |  |
| 11-10 16:31 | +15 | HYPE | UP | 0.68 | open |  |
| 11-10 16:31 | +10 | HYPE | UP | 0.67 | open |  |
