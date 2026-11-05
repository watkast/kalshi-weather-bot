# Range-Scalp Bot

*Updated Thu Nov 05 16:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48580 | 42338 | 6242 (73) | 1 | $-13769.02 | -4.5% |
| **+10¢** | 36257 | 29003 | 7254 (99) | 1 | $-12620.37 | -5.5% |
| **+15¢** | 30371 | 22556 | 7815 (127) | 1 | $-11535.51 | -6.1% |
| **+20¢** | 26984 | 18795 | 8189 (166) | 1 | $-10189.31 | -6.0% |
| **+10¢ (15¢ stop)** | 59189 | 59096 | 93 (56) | 1 | $-21931.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 16:37 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-05 16:37 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-05 16:37 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 11-05 16:37 | +5 | HYPE | DOWN | 0.64 | open |  |
| 11-05 16:36 | +10 stop | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 11-05 16:36 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-05 16:36 | +5 | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-05 16:36 | +10 stop | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-05 16:36 | +15 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-05 16:36 | +10 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-05 16:36 | +5 | ETH | DOWN | 0.56 | 0.61 | 0.15 |
| 11-05 16:35 | +10 stop | XRP | UP | 0.56 | 0.39 | -2.05 |
| 11-05 16:35 | +10 stop | DOGE | UP | 0.45 | 0.57 | 0.84 |
| 11-05 16:35 | +10 stop | BNB | UP | 0.43 | 0.55 | 0.79 |
| 11-05 16:35 | +5 | HYPE | UP | 0.55 | 0.63 | 0.45 |
| 11-05 16:35 | +5 | BNB | UP | 0.50 | 0.55 | 0.14 |
| 11-05 16:35 | +10 stop | SOL | UP | 0.60 | 0.41 | -2.24 |
| 11-05 16:35 | +10 stop | BTC | UP | 0.62 | 0.40 | -2.54 |
| 11-05 16:35 | +10 stop | ETH | DOWN | 0.46 | 0.62 | 1.25 |
| 11-05 16:35 | +20 | ETH | DOWN | 0.46 | 0.74 | 2.48 |
| 11-05 16:35 | +15 | ETH | DOWN | 0.46 | 0.62 | 1.25 |
| 11-05 16:35 | +10 | ETH | DOWN | 0.46 | 0.62 | 1.25 |
| 11-05 16:35 | +5 | ETH | DOWN | 0.45 | 0.62 | 1.35 |
| 11-05 16:35 | +5 | BNB | DOWN | 0.55 | 0.68 | 0.96 |
| 11-05 16:35 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-05 16:34 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 11-05 16:34 | +10 stop | DOGE | DOWN | 0.69 | 0.37 | -3.52 |
| 11-05 16:34 | +10 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-05 16:34 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-05 16:34 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-05 16:32 | +10 stop | XRP | DOWN | 0.68 | 0.32 | -3.92 |
| 11-05 16:32 | +20 | XRP | DOWN | 0.68 | 0.92 | 2.13 |
| 11-05 16:32 | +15 | XRP | DOWN | 0.68 | 0.87 | 1.66 |
| 11-05 16:32 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-05 16:32 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 11-05 16:32 | +10 stop | HYPE | UP | 0.58 | 0.40 | -2.15 |
| 11-05 16:32 | +20 | HYPE | UP | 0.58 | open |  |
| 11-05 16:32 | +15 | HYPE | UP | 0.58 | open |  |
| 11-05 16:32 | +10 | HYPE | UP | 0.58 | open |  |
| 11-05 16:32 | +5 | HYPE | UP | 0.58 | 0.63 | 0.15 |
