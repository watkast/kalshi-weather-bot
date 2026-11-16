# Range-Scalp Bot

*Updated Mon Nov 16 21:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62292 | 54343 | 7949 (117) | 6 | $-16877.22 | -4.3% |
| **+10¢** | 46513 | 37213 | 9300 (159) | 8 | $-15747.16 | -5.4% |
| **+15¢** | 38972 | 28940 | 10032 (200) | 8 | $-14341.22 | -5.9% |
| **+20¢** | 34739 | 24219 | 10520 (255) | 8 | $-12520.80 | -5.7% |
| **+10¢ (15¢ stop)** | 75823 | 75667 | 156 (92) | 1 | $-27982.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 21:41 | +10 stop | DOGE | UP | 0.66 | open |  |
| 11-16 21:41 | +10 | DOGE | UP | 0.66 | open |  |
| 11-16 21:41 | +5 | DOGE | UP | 0.66 | open |  |
| 11-16 21:39 | +5 | XRP | DOWN | 0.23 | 0.59 | 3.30 |
| 11-16 21:39 | +10 stop | ETH | UP | 0.71 | 0.86 | 1.28 |
| 11-16 21:39 | +10 stop | BTC | UP | 0.65 | 0.85 | 1.75 |
| 11-16 21:38 | +10 stop | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-16 21:38 | +10 stop | XRP | DOWN | 0.67 | 0.21 | -4.88 |
| 11-16 21:38 | +20 | XRP | DOWN | 0.67 | open |  |
| 11-16 21:38 | +15 | XRP | DOWN | 0.67 | open |  |
| 11-16 21:38 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-16 21:38 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 11-16 21:38 | +15 | BNB | DOWN | 0.59 | open |  |
| 11-16 21:38 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-16 21:37 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-16 21:37 | +5 | NEAR | DOWN | 0.63 | open |  |
| 11-16 21:36 | +10 stop | NEAR | DOWN | 0.65 | 0.50 | -1.84 |
| 11-16 21:36 | +10 stop | ETH | DOWN | 0.65 | 0.40 | -2.83 |
| 11-16 21:36 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-16 21:36 | +5 | ETH | DOWN | 0.64 | open |  |
| 11-16 21:36 | +10 stop | BNB | DOWN | 0.68 | 0.53 | -1.84 |
| 11-16 21:36 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-16 21:36 | +5 | BNB | DOWN | 0.70 | open |  |
| 11-16 21:36 | +5 | SOL | UP | 0.62 | 0.69 | 0.38 |
| 11-16 21:36 | +10 stop | SOL | UP | 0.59 | 0.69 | 0.68 |
| 11-16 21:35 | +5 | SOL | UP | 0.62 | 0.67 | 0.18 |
| 11-16 21:35 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-16 21:35 | +5 | BNB | DOWN | 0.53 | 0.58 | 0.14 |
| 11-16 21:34 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 21:34 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-16 21:34 | +15 | DOGE | DOWN | 0.71 | open |  |
| 11-16 21:34 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 21:34 | +5 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-16 21:34 | +10 stop | BTC | DOWN | 0.68 | 0.49 | -2.24 |
| 11-16 21:34 | +15 | BTC | DOWN | 0.68 | open |  |
| 11-16 21:34 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-16 21:34 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-16 21:34 | +10 stop | SOL | UP | 0.55 | 0.67 | 0.86 |
| 11-16 21:34 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-16 21:34 | +15 | XRP | DOWN | 0.66 | 0.83 | 1.44 |
