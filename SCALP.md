# Range-Scalp Bot

*Updated Sun Oct 25 17:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33482 | 29216 | 4266 (42) | 6 | $-9388.76 | -4.5% |
| **+10¢** | 25060 | 20124 | 4936 (60) | 7 | $-8332.42 | -5.3% |
| **+15¢** | 20961 | 15647 | 5314 (83) | 7 | $-7499.81 | -5.7% |
| **+20¢** | 18576 | 13012 | 5564 (105) | 7 | $-6602.92 | -5.7% |
| **+10¢ (15¢ stop)** | 41045 | 40985 | 60 (32) | 3 | $-15647.51 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 17:40 | +10 stop | HYPE | DOWN | 0.70 | 0.47 | -2.68 |
| 10-25 17:40 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-25 17:40 | +5 | HYPE | DOWN | 0.70 | open |  |
| 10-25 17:40 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 10-25 17:40 | +10 stop | SOL | UP | 0.68 | open |  |
| 10-25 17:40 | +15 | SOL | UP | 0.68 | open |  |
| 10-25 17:40 | +5 | SOL | UP | 0.68 | open |  |
| 10-25 17:39 | +10 stop | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 10-25 17:39 | +5 | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-25 17:39 | +10 stop | XRP | DOWN | 0.63 | 0.79 | 1.26 |
| 10-25 17:39 | +20 | XRP | DOWN | 0.64 | 0.84 | 1.73 |
| 10-25 17:39 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-25 17:39 | +10 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-25 17:39 | +5 | XRP | DOWN | 0.64 | 0.70 | 0.28 |
| 10-25 17:39 | +10 stop | ZEC | UP | 0.69 | 0.49 | -2.33 |
| 10-25 17:38 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-25 17:38 | +10 stop | NEAR | UP | 0.56 | 0.41 | -1.88 |
| 10-25 17:38 | +5 | NEAR | UP | 0.55 | 0.61 | 0.25 |
| 10-25 17:38 | +10 stop | BTC | DOWN | 0.58 | open |  |
| 10-25 17:37 | +10 stop | DOGE | UP | 0.58 | 0.42 | -1.96 |
| 10-25 17:37 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-25 17:37 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-25 17:36 | +10 stop | DOGE | DOWN | 0.44 | 0.58 | 1.04 |
| 10-25 17:35 | +10 | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-25 17:35 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-25 17:35 | +5 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-25 17:35 | +10 stop | BTC | DOWN | 0.62 | 0.45 | -2.05 |
| 10-25 17:34 | +10 stop | XRP | DOWN | 0.70 | 0.84 | 1.15 |
| 10-25 17:34 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 10-25 17:34 | +10 | DOGE | UP | 0.64 | open |  |
| 10-25 17:33 | +5 | DOGE | UP | 0.67 | open |  |
| 10-25 17:33 | +10 stop | SOL | UP | 0.68 | 0.50 | -2.14 |
| 10-25 17:33 | +10 | SOL | UP | 0.68 | open |  |
| 10-25 17:33 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 10-25 17:33 | +10 stop | ETH | UP | 0.62 | 0.38 | -2.74 |
| 10-25 17:33 | +10 | ETH | UP | 0.62 | open |  |
| 10-25 17:33 | +10 stop | BNB | UP | 0.54 | 0.26 | -3.12 |
| 10-25 17:33 | +20 | BNB | UP | 0.54 | open |  |
| 10-25 17:33 | +15 | BNB | UP | 0.55 | open |  |
| 10-25 17:33 | +10 | BNB | UP | 0.55 | open |  |
