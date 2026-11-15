# Range-Scalp Bot

*Updated Sun Nov 15 23:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61385 | 53565 | 7820 (115) | 5 | $-16508.32 | -4.3% |
| **+10¢** | 45845 | 36680 | 9165 (156) | 5 | $-15499.49 | -5.4% |
| **+15¢** | 38405 | 28517 | 9888 (195) | 6 | $-14156.23 | -5.9% |
| **+20¢** | 34230 | 23858 | 10372 (247) | 7 | $-12424.92 | -5.8% |
| **+10¢ (15¢ stop)** | 74703 | 74549 | 154 (90) | 0 | $-27483.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 23:39 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-15 23:39 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 11-15 23:39 | +10 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-15 23:39 | +5 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-15 23:37 | +10 stop | HYPE | DOWN | 0.47 | 0.60 | 0.95 |
| 11-15 23:37 | +20 | HYPE | DOWN | 0.44 | open |  |
| 11-15 23:37 | +15 | HYPE | DOWN | 0.44 | 0.60 | 1.25 |
| 11-15 23:37 | +10 | HYPE | DOWN | 0.44 | 0.60 | 1.25 |
| 11-15 23:37 | +5 | HYPE | DOWN | 0.44 | 0.60 | 1.25 |
| 11-15 23:37 | +10 stop | BNB | DOWN | 0.46 | 0.23 | -2.61 |
| 11-15 23:37 | +20 | BNB | DOWN | 0.46 | open |  |
| 11-15 23:37 | +15 | BNB | DOWN | 0.46 | open |  |
| 11-15 23:37 | +10 | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 11-15 23:37 | +5 | BNB | DOWN | 0.45 | 0.55 | 0.64 |
| 11-15 23:36 | +10 stop | ETH | UP | 0.68 | 0.84 | 1.34 |
| 11-15 23:36 | +10 stop | ZEC | DOWN | 0.60 | 0.42 | -2.15 |
| 11-15 23:36 | +5 | ZEC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-15 23:36 | +10 stop | SOL | DOWN | 0.56 | 0.33 | -2.64 |
| 11-15 23:36 | +10 | SOL | DOWN | 0.56 | open |  |
| 11-15 23:36 | +5 | SOL | DOWN | 0.56 | open |  |
| 11-15 23:36 | +10 stop | XRP | DOWN | 0.56 | 0.19 | -3.99 |
| 11-15 23:36 | +20 | XRP | DOWN | 0.56 | open |  |
| 11-15 23:36 | +15 | XRP | DOWN | 0.56 | open |  |
| 11-15 23:36 | +10 | XRP | DOWN | 0.56 | open |  |
| 11-15 23:36 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-15 23:36 | +10 stop | DOGE | DOWN | 0.70 | 0.46 | -2.73 |
| 11-15 23:35 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
| 11-15 23:35 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-15 23:35 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-15 23:35 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-15 23:35 | +10 stop | NEAR | DOWN | 0.59 | 0.37 | -2.54 |
| 11-15 23:35 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-15 23:35 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-15 23:35 | +5 | NEAR | DOWN | 0.59 | open |  |
| 11-15 23:34 | +5 | DOGE | UP | 0.67 | 0.86 | 1.65 |
| 11-15 23:34 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 23:33 | +10 stop | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-15 23:33 | +10 stop | DOGE | UP | 0.64 | 0.18 | -4.85 |
| 11-15 23:33 | +20 | DOGE | UP | 0.64 | 0.86 | 1.97 |
| 11-15 23:33 | +15 | DOGE | UP | 0.62 | 0.86 | 2.14 |
