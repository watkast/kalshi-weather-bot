# Range-Scalp Bot

*Updated Sun Oct 25 07:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32788 | 28592 | 4196 (42) | 4 | $-9317.98 | -4.5% |
| **+10¢** | 24546 | 19688 | 4858 (60) | 5 | $-8324.53 | -5.4% |
| **+15¢** | 20546 | 15319 | 5227 (83) | 7 | $-7488.93 | -5.8% |
| **+20¢** | 18200 | 12728 | 5472 (105) | 8 | $-6636.55 | -5.8% |
| **+10¢ (15¢ stop)** | 40269 | 40209 | 60 (32) | 5 | $-15386.65 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 07:35 | +5 | ZEC | UP | 0.60 | 0.67 | 0.37 |
| 10-25 07:35 | +10 stop | ZEC | UP | 0.69 | open |  |
| 10-25 07:34 | +5 | NEAR | UP | 0.66 | open |  |
| 10-25 07:34 | +10 | XRP | UP | 0.71 | open |  |
| 10-25 07:34 | +5 | XRP | UP | 0.71 | 0.77 | 0.32 |
| 10-25 07:34 | +10 stop | XRP | UP | 0.71 | open |  |
| 10-25 07:34 | +10 stop | ZEC | UP | 0.52 | 0.64 | 0.85 |
| 10-25 07:33 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 10-25 07:33 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-25 07:33 | +10 stop | SOL | DOWN | 0.48 | 0.31 | -2.03 |
| 10-25 07:33 | +10 stop | DOGE | DOWN | 0.52 | 0.29 | -2.63 |
| 10-25 07:33 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-25 07:33 | +10 stop | HYPE | DOWN | 0.60 | open |  |
| 10-25 07:33 | +10 stop | XRP | UP | 0.55 | 0.70 | 1.17 |
| 10-25 07:33 | +10 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 10-25 07:33 | +5 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 10-25 07:32 | +10 stop | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-25 07:32 | +15 | XRP | UP | 0.58 | 0.77 | 1.59 |
| 10-25 07:32 | +10 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-25 07:32 | +5 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-25 07:32 | +10 stop | ZEC | UP | 0.61 | 0.44 | -2.05 |
| 10-25 07:32 | +10 | ZEC | UP | 0.61 | open |  |
| 10-25 07:32 | +10 stop | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-25 07:32 | +10 | BTC | UP | 0.64 | 0.78 | 1.10 |
| 10-25 07:32 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 10-25 07:32 | +10 stop | ETH | UP | 0.52 | 0.35 | -2.04 |
| 10-25 07:32 | +10 | ETH | UP | 0.52 | open |  |
| 10-25 07:32 | +5 | ETH | UP | 0.52 | open |  |
| 10-25 07:32 | +5 | HYPE | UP | 0.57 | open |  |
| 10-25 07:32 | +5 | NEAR | UP | 0.61 | 0.66 | 0.18 |
| 10-25 07:32 | +5 | ZEC | UP | 0.61 | 0.67 | 0.27 |
| 10-25 07:32 | +5 | SOL | UP | 0.68 | open |  |
| 10-25 07:32 | +5 | BNB | UP | 0.65 | 0.81 | 1.33 |
| 10-25 07:31 | +10 stop | NEAR | UP | 0.62 | open |  |
| 10-25 07:31 | +20 | NEAR | UP | 0.62 | open |  |
| 10-25 07:31 | +15 | NEAR | UP | 0.62 | open |  |
| 10-25 07:31 | +10 | NEAR | UP | 0.62 | open |  |
| 10-25 07:31 | +5 | NEAR | UP | 0.62 | 0.67 | 0.17 |
| 10-25 07:31 | +10 stop | BTC | UP | 0.57 | 0.71 | 1.07 |
| 10-25 07:31 | +10 | BTC | UP | 0.57 | 0.71 | 1.07 |
