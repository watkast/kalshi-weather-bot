# Range-Scalp Bot

*Updated Thu Nov 05 16:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48559 | 42317 | 6242 (73) | 0 | $-13780.50 | -4.5% |
| **+10¢** | 36245 | 28991 | 7254 (99) | 2 | $-12632.43 | -5.5% |
| **+15¢** | 30360 | 22547 | 7813 (127) | 2 | $-11536.37 | -6.1% |
| **+20¢** | 26972 | 18785 | 8187 (166) | 4 | $-10197.67 | -6.0% |
| **+10¢ (15¢ stop)** | 59163 | 59070 | 93 (56) | 1 | $-21912.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 16:20 | +10 stop | BNB | UP | 0.66 | open |  |
| 11-05 16:20 | +10 | BNB | UP | 0.66 | open |  |
| 11-05 16:20 | +5 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-05 16:19 | +10 stop | HYPE | DOWN | 0.62 | 0.46 | -1.95 |
| 11-05 16:19 | +20 | HYPE | DOWN | 0.63 | open |  |
| 11-05 16:19 | +15 | HYPE | DOWN | 0.63 | open |  |
| 11-05 16:19 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-05 16:19 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-05 16:18 | +5 | BNB | UP | 0.64 | 0.72 | 0.48 |
| 11-05 16:18 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-05 16:18 | +15 | ETH | UP | 0.70 | 0.87 | 1.47 |
| 11-05 16:18 | +10 | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-05 16:18 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 11-05 16:17 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.85 |
| 11-05 16:17 | +10 | XRP | UP | 0.65 | 0.76 | 0.85 |
| 11-05 16:17 | +5 | XRP | UP | 0.65 | 0.71 | 0.33 |
| 11-05 16:17 | +10 stop | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 11-05 16:17 | +20 | DOGE | UP | 0.64 | open |  |
| 11-05 16:17 | +15 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 11-05 16:17 | +10 | DOGE | UP | 0.64 | 0.79 | 1.21 |
| 11-05 16:17 | +5 | DOGE | UP | 0.64 | 0.73 | 0.59 |
| 11-05 16:16 | +10 stop | SOL | UP | 0.52 | 0.68 | 1.26 |
| 11-05 16:16 | +20 | SOL | UP | 0.52 | 0.72 | 1.67 |
| 11-05 16:16 | +15 | SOL | UP | 0.52 | 0.68 | 1.26 |
| 11-05 16:16 | +10 | SOL | UP | 0.52 | 0.68 | 1.26 |
| 11-05 16:16 | +5 | SOL | UP | 0.52 | 0.57 | 0.14 |
| 11-05 16:16 | +10 stop | ETH | UP | 0.52 | 0.68 | 1.26 |
| 11-05 16:16 | +20 | ETH | UP | 0.52 | 0.79 | 2.40 |
| 11-05 16:16 | +15 | ETH | UP | 0.52 | 0.68 | 1.26 |
| 11-05 16:16 | +10 | ETH | UP | 0.52 | 0.68 | 1.26 |
| 11-05 16:16 | +5 | ETH | UP | 0.52 | 0.60 | 0.45 |
| 11-05 16:16 | +5 | ZEC | UP | 0.70 | 0.79 | 0.63 |
| 11-05 16:16 | +10 stop | BNB | UP | 0.53 | 0.64 | 0.75 |
| 11-05 16:16 | +20 | BNB | UP | 0.53 | open |  |
| 11-05 16:16 | +15 | BNB | UP | 0.53 | 0.72 | 1.57 |
| 11-05 16:16 | +10 | BNB | UP | 0.53 | 0.64 | 0.75 |
| 11-05 16:16 | +5 | BNB | UP | 0.53 | 0.59 | 0.25 |
| 11-05 16:16 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-05 16:16 | +20 | BTC | UP | 0.60 | 0.82 | 1.92 |
| 11-05 16:16 | +15 | BTC | UP | 0.60 | 0.75 | 1.19 |
