# Range-Scalp Bot

*Updated Mon Nov 23 22:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70231 | 61290 | 8941 (147) | 6 | $-18861.63 | -4.3% |
| **+10¢** | 52400 | 41959 | 10441 (190) | 8 | $-17492.92 | -5.3% |
| **+15¢** | 43902 | 32659 | 11243 (246) | 9 | $-15574.09 | -5.7% |
| **+20¢** | 39086 | 27252 | 11834 (311) | 9 | $-13956.42 | -5.7% |
| **+10¢ (15¢ stop)** | 85546 | 85350 | 196 (118) | 7 | $-31495.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 22:50 | +5 | XRP | UP | 0.51 | 0.58 | 0.34 |
| 11-23 22:50 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-23 22:50 | +10 | ETH | UP | 0.66 | open |  |
| 11-23 22:50 | +5 | ETH | UP | 0.66 | open |  |
| 11-23 22:50 | +10 stop | BTC | UP | 0.61 | 0.45 | -1.95 |
| 11-23 22:50 | +5 | NEAR | DOWN | 0.54 | 0.62 | 0.45 |
| 11-23 22:50 | +10 stop | NEAR | DOWN | 0.61 | open |  |
| 11-23 22:49 | +10 stop | XRP | UP | 0.51 | open |  |
| 11-23 22:49 | +10 stop | SOL | DOWN | 0.69 | open |  |
| 11-23 22:49 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-23 22:49 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 11-23 22:48 | +10 stop | BNB | UP | 0.56 | open |  |
| 11-23 22:48 | +5 | NEAR | DOWN | 0.51 | 0.65 | 1.06 |
| 11-23 22:48 | +10 stop | HYPE | UP | 0.62 | open |  |
| 11-23 22:48 | +10 stop | ETH | DOWN | 0.46 | 0.59 | 0.95 |
| 11-23 22:48 | +10 | ETH | DOWN | 0.46 | 0.59 | 0.95 |
| 11-23 22:48 | +5 | ETH | DOWN | 0.46 | 0.59 | 0.95 |
| 11-23 22:48 | +5 | NEAR | DOWN | 0.52 | 0.59 | 0.40 |
| 11-23 22:48 | +10 stop | DOGE | DOWN | 0.70 | open |  |
| 11-23 22:48 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-23 22:48 | +5 | DOGE | DOWN | 0.71 | open |  |
| 11-23 22:47 | +5 | XRP | DOWN | 0.47 | 0.61 | 1.05 |
| 11-23 22:47 | +10 stop | ETH | DOWN | 0.48 | 0.64 | 1.25 |
| 11-23 22:47 | +10 | ETH | DOWN | 0.48 | 0.64 | 1.25 |
| 11-23 22:47 | +5 | ETH | DOWN | 0.48 | 0.64 | 1.25 |
| 11-23 22:47 | +10 stop | HYPE | DOWN | 0.61 | 0.44 | -2.05 |
| 11-23 22:47 | +10 stop | XRP | DOWN | 0.60 | 0.40 | -2.34 |
| 11-23 22:47 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-23 22:47 | +15 | XRP | DOWN | 0.60 | open |  |
| 11-23 22:47 | +10 | XRP | DOWN | 0.60 | open |  |
| 11-23 22:47 | +5 | XRP | DOWN | 0.59 | 0.64 | 0.16 |
| 11-23 22:47 | +10 stop | BNB | DOWN | 0.63 | 0.47 | -1.95 |
| 11-23 22:47 | +10 stop | BTC | DOWN | 0.55 | 0.37 | -2.15 |
| 11-23 22:47 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-23 22:47 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-23 22:47 | +10 stop | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 11-23 22:47 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-23 22:47 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-23 22:47 | +10 | ETH | DOWN | 0.55 | 0.68 | 0.96 |
| 11-23 22:47 | +5 | ETH | DOWN | 0.55 | 0.68 | 0.96 |
