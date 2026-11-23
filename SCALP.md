# Range-Scalp Bot

*Updated Mon Nov 23 21:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70110 | 61184 | 8926 (147) | 5 | $-18837.57 | -4.3% |
| **+10¢** | 52309 | 41884 | 10425 (190) | 8 | $-17482.90 | -5.3% |
| **+15¢** | 43831 | 32603 | 11228 (246) | 9 | $-15576.39 | -5.7% |
| **+20¢** | 39025 | 27209 | 11816 (311) | 9 | $-13939.36 | -5.7% |
| **+10¢ (15¢ stop)** | 85391 | 85195 | 196 (118) | 6 | $-31396.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 21:18 | +10 stop | DOGE | DOWN | 0.69 | open |  |
| 11-23 21:18 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-23 21:18 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-23 21:18 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-23 21:18 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 21:17 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 11-23 21:17 | +5 | HYPE | DOWN | 0.60 | 0.68 | 0.47 |
| 11-23 21:17 | +10 stop | XRP | DOWN | 0.52 | open |  |
| 11-23 21:17 | +20 | XRP | DOWN | 0.52 | open |  |
| 11-23 21:17 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-23 21:17 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-23 21:17 | +5 | XRP | DOWN | 0.52 | open |  |
| 11-23 21:16 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 11-23 21:16 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-23 21:16 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-23 21:16 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-23 21:16 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-23 21:16 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-23 21:16 | +10 stop | ZEC | DOWN | 0.53 | open |  |
| 11-23 21:16 | +10 stop | NEAR | DOWN | 0.64 | open |  |
| 11-23 21:16 | +10 stop | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-23 21:16 | +20 | HYPE | DOWN | 0.60 | open |  |
| 11-23 21:16 | +15 | HYPE | DOWN | 0.60 | open |  |
| 11-23 21:16 | +10 | HYPE | DOWN | 0.59 | 0.73 | 1.04 |
| 11-23 21:16 | +5 | HYPE | DOWN | 0.59 | 0.66 | 0.32 |
| 11-23 21:16 | +10 stop | SOL | DOWN | 0.64 | 0.49 | -1.85 |
| 11-23 21:16 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-23 21:16 | +5 | SOL | DOWN | 0.65 | open |  |
| 11-23 21:16 | +5 | BNB | DOWN | 0.69 | open |  |
| 11-23 21:15 | +10 stop | SOL | UP | 0.46 | 0.56 | 0.64 |
| 11-23 21:15 | +20 | SOL | UP | 0.46 | open |  |
| 11-23 21:15 | +15 | SOL | UP | 0.46 | open |  |
| 11-23 21:15 | +10 | SOL | UP | 0.46 | 0.56 | 0.64 |
| 11-23 21:15 | +5 | SOL | UP | 0.46 | 0.56 | 0.64 |
| 11-23 21:15 | +10 stop | BNB | UP | 0.54 | 0.37 | -2.05 |
| 11-23 21:15 | +20 | BNB | UP | 0.54 | open |  |
| 11-23 21:15 | +15 | BNB | UP | 0.54 | open |  |
| 11-23 21:15 | +10 | BNB | UP | 0.54 | open |  |
| 11-23 21:15 | +5 | BNB | UP | 0.54 | 0.61 | 0.35 |
| 11-23 21:15 | +10 stop | ETH | UP | 0.53 | 0.34 | -2.24 |
