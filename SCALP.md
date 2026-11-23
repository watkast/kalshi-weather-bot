# Range-Scalp Bot

*Updated Mon Nov 23 21:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70163 | 61229 | 8934 (147) | 1 | $-18860.62 | -4.3% |
| **+10¢** | 52349 | 41915 | 10434 (190) | 2 | $-17503.42 | -5.3% |
| **+15¢** | 43867 | 32629 | 11238 (246) | 1 | $-15595.78 | -5.7% |
| **+20¢** | 39053 | 27226 | 11827 (311) | 2 | $-13969.16 | -5.7% |
| **+10¢ (15¢ stop)** | 85457 | 85261 | 196 (118) | 0 | $-31437.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 21:58 | +10 stop | DOGE | DOWN | 0.53 | 0.02 | -5.32 |
| 11-23 21:58 | +10 stop | BTC | DOWN | 0.47 | 0.62 | 1.15 |
| 11-23 21:58 | +20 | BTC | DOWN | 0.47 | open |  |
| 11-23 21:58 | +15 | BTC | DOWN | 0.47 | 0.62 | 1.15 |
| 11-23 21:58 | +10 | BTC | DOWN | 0.45 | 0.62 | 1.35 |
| 11-23 21:58 | +5 | BTC | DOWN | 0.44 | 0.62 | 1.45 |
| 11-23 21:56 | +10 stop | XRP | UP | 0.63 | 0.48 | -1.85 |
| 11-23 21:55 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-23 21:55 | +15 | ETH | UP | 0.62 | 0.81 | 1.62 |
| 11-23 21:55 | +5 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-23 21:54 | +10 stop | SOL | UP | 0.57 | 0.40 | -2.05 |
| 11-23 21:54 | +15 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-23 21:54 | +10 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-23 21:54 | +5 | SOL | UP | 0.57 | 0.72 | 1.17 |
| 11-23 21:54 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 11-23 21:54 | +10 | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 11-23 21:54 | +5 | BNB | DOWN | 0.61 | 0.66 | 0.17 |
| 11-23 21:54 | +10 stop | NEAR | DOWN | 0.54 | 0.72 | 1.47 |
| 11-23 21:53 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 11-23 21:53 | +20 | DOGE | UP | 0.58 | 0.98 | 3.76 |
| 11-23 21:53 | +15 | DOGE | UP | 0.58 | 0.98 | 3.76 |
| 11-23 21:53 | +10 | DOGE | UP | 0.58 | 0.98 | 3.76 |
| 11-23 21:53 | +5 | DOGE | UP | 0.59 | 0.98 | 3.67 |
| 11-23 21:53 | +10 stop | BNB | DOWN | 0.54 | 0.65 | 0.76 |
| 11-23 21:53 | +20 | BNB | DOWN | 0.54 | 0.75 | 1.78 |
| 11-23 21:53 | +15 | BNB | DOWN | 0.54 | 0.75 | 1.78 |
| 11-23 21:53 | +10 | BNB | DOWN | 0.53 | 0.65 | 0.86 |
| 11-23 21:53 | +5 | BNB | DOWN | 0.53 | 0.65 | 0.86 |
| 11-23 21:53 | +10 stop | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-23 21:53 | +20 | BTC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-23 21:53 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-23 21:53 | +10 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-23 21:53 | +5 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-23 21:53 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-23 21:53 | +20 | HYPE | DOWN | 0.59 | 0.84 | 2.23 |
| 11-23 21:53 | +15 | HYPE | DOWN | 0.59 | 0.75 | 1.29 |
| 11-23 21:53 | +10 | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 11-23 21:53 | +5 | HYPE | DOWN | 0.58 | 0.66 | 0.46 |
| 11-23 21:53 | +20 | ETH | UP | 0.70 | 0.93 | 2.12 |
| 11-23 21:53 | +15 | ETH | UP | 0.70 | 0.87 | 1.47 |
