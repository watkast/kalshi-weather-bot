# Range-Scalp Bot

*Updated Sun Oct 11 01:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11175 | 9634 | 1541 (22) | 1 | $-3801.92 | -5.4% |
| **+10¢** | 8469 | 6673 | 1796 (36) | 1 | $-3640.01 | -6.8% |
| **+15¢** | 7136 | 5238 | 1898 (52) | 1 | $-3072.10 | -6.9% |
| **+20¢** | 6354 | 4379 | 1975 (66) | 1 | $-2587.46 | -6.5% |
| **+10¢ (15¢ stop)** | 13769 | 13728 | 41 (25) | 1 | $-5506.50 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 01:01 | +10 stop | BNB | UP | 0.66 | open |  |
| 10-11 01:01 | +20 | BNB | UP | 0.65 | open |  |
| 10-11 01:01 | +15 | BNB | UP | 0.66 | open |  |
| 10-11 01:01 | +10 | BNB | UP | 0.65 | open |  |
| 10-11 01:01 | +5 | BNB | UP | 0.65 | open |  |
| 10-11 00:58 | +15 | NEAR | UP | 0.62 | no | -6.37 |
| 10-11 00:58 | +10 | NEAR | UP | 0.60 | no | -6.17 |
| 10-11 00:58 | +5 | NEAR | UP | 0.53 | 0.66 | 0.96 |
| 10-11 00:56 | +10 stop | BTC | UP | 0.63 | 0.48 | -1.85 |
| 10-11 00:56 | +10 stop | NEAR | UP | 0.71 | 0.47 | -2.73 |
| 10-11 00:55 | +10 stop | NEAR | DOWN | 0.52 | 0.62 | 0.68 |
| 10-11 00:55 | +10 stop | SOL | UP | 0.67 | 0.84 | 1.44 |
| 10-11 00:55 | +10 | SOL | UP | 0.67 | 0.84 | 1.44 |
| 10-11 00:55 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-11 00:54 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-11 00:54 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-11 00:54 | +10 stop | XRP | UP | 0.53 | 0.28 | -2.83 |
| 10-11 00:54 | +10 | XRP | UP | 0.53 | no | -5.48 |
| 10-11 00:54 | +5 | XRP | UP | 0.53 | no | -5.48 |
| 10-11 00:53 | +10 stop | HYPE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-11 00:53 | +5 | HYPE | DOWN | 0.49 | 0.62 | 0.95 |
| 10-11 00:53 | +10 stop | BNB | DOWN | 0.61 | 0.80 | 1.61 |
| 10-11 00:53 | +10 stop | XRP | DOWN | 0.52 | 0.65 | 0.96 |
| 10-11 00:53 | +20 | XRP | DOWN | 0.52 | 0.74 | 1.88 |
| 10-11 00:53 | +15 | XRP | DOWN | 0.52 | 0.70 | 1.47 |
| 10-11 00:53 | +10 | XRP | DOWN | 0.52 | 0.65 | 0.96 |
| 10-11 00:53 | +5 | XRP | DOWN | 0.52 | 0.65 | 0.96 |
| 10-11 00:53 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.94 |
| 10-11 00:53 | +15 | SOL | UP | 0.66 | 0.84 | 1.57 |
| 10-11 00:53 | +10 | SOL | UP | 0.66 | 0.78 | 0.94 |
| 10-11 00:53 | +5 | SOL | UP | 0.66 | 0.78 | 0.94 |
| 10-11 00:53 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 10-11 00:53 | +20 | BTC | UP | 0.61 | no | -6.27 |
| 10-11 00:53 | +15 | BTC | UP | 0.61 | no | -6.27 |
| 10-11 00:53 | +10 | BTC | UP | 0.61 | no | -6.27 |
| 10-11 00:53 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 10-11 00:53 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-11 00:53 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 10-11 00:53 | +5 | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-11 00:52 | +10 stop | XRP | UP | 0.47 | 0.68 | 1.76 |
