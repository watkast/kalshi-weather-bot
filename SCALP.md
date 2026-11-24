# Range-Scalp Bot

*Updated Tue Nov 24 01:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70390 | 61440 | 8950 (147) | 5 | $-18825.18 | -4.2% |
| **+10¢** | 52516 | 42063 | 10453 (190) | 4 | $-17454.83 | -5.3% |
| **+15¢** | 43996 | 32737 | 11259 (246) | 4 | $-15537.09 | -5.6% |
| **+20¢** | 39175 | 27323 | 11852 (311) | 5 | $-13910.30 | -5.7% |
| **+10¢ (15¢ stop)** | 85725 | 85529 | 196 (118) | 0 | $-31541.13 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 01:21 | +10 stop | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 11-24 01:20 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
| 11-24 01:20 | +10 stop | BTC | UP | 0.64 | 0.75 | 0.79 |
| 11-24 01:19 | +5 | BNB | UP | 0.61 | 0.68 | 0.37 |
| 11-24 01:19 | +10 stop | ZEC | DOWN | 0.66 | 0.43 | -2.63 |
| 11-24 01:19 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-24 01:19 | +5 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-24 01:19 | +5 | BNB | UP | 0.55 | 0.63 | 0.45 |
| 11-24 01:18 | +10 stop | XRP | UP | 0.55 | 0.79 | 2.10 |
| 11-24 01:18 | +10 stop | DOGE | UP | 0.59 | 0.72 | 0.98 |
| 11-24 01:18 | +10 stop | SOL | DOWN | 0.53 | 0.38 | -1.85 |
| 11-24 01:17 | +10 stop | BNB | UP | 0.57 | 0.68 | 0.72 |
| 11-24 01:17 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-24 01:17 | +10 stop | NEAR | UP | 0.64 | 0.75 | 0.79 |
| 11-24 01:17 | +20 | NEAR | UP | 0.65 | 0.85 | 1.75 |
| 11-24 01:17 | +15 | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 11-24 01:17 | +10 | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 11-24 01:17 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 11-24 01:17 | +10 stop | BNB | DOWN | 0.60 | 0.44 | -1.95 |
| 11-24 01:17 | +10 stop | XRP | DOWN | 0.66 | 0.46 | -2.31 |
| 11-24 01:17 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-24 01:17 | +15 | XRP | DOWN | 0.66 | open |  |
| 11-24 01:17 | +10 | XRP | DOWN | 0.66 | open |  |
| 11-24 01:17 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-24 01:16 | +10 stop | HYPE | DOWN | 0.58 | 0.37 | -2.45 |
| 11-24 01:16 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 11-24 01:16 | +10 stop | DOGE | DOWN | 0.61 | 0.42 | -2.25 |
| 11-24 01:16 | +20 | DOGE | DOWN | 0.61 | open |  |
| 11-24 01:16 | +15 | DOGE | DOWN | 0.61 | open |  |
| 11-24 01:16 | +10 | DOGE | DOWN | 0.61 | open |  |
| 11-24 01:16 | +5 | DOGE | DOWN | 0.61 | open |  |
| 11-24 01:16 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 11-24 01:16 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-24 01:16 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-24 01:16 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-24 01:16 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-24 01:16 | +5 | SOL | DOWN | 0.66 | open |  |
| 11-24 01:16 | +10 stop | BTC | DOWN | 0.65 | 0.42 | -2.64 |
| 11-24 01:16 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-24 01:16 | +15 | BTC | DOWN | 0.65 | open |  |
