# Range-Scalp Bot

*Updated Wed Nov 11 00:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55089 | 48047 | 7042 (94) | 5 | $-15032.19 | -4.3% |
| **+10¢** | 41165 | 32954 | 8211 (124) | 5 | $-13915.53 | -5.4% |
| **+15¢** | 34509 | 25659 | 8850 (158) | 6 | $-12650.56 | -5.8% |
| **+20¢** | 30721 | 21436 | 9285 (207) | 6 | $-11060.49 | -5.7% |
| **+10¢ (15¢ stop)** | 67106 | 66988 | 118 (73) | 3 | $-24759.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 00:06 | +10 stop | HYPE | UP | 0.42 | 0.55 | 0.94 |
| 11-11 00:06 | +10 stop | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-11 00:06 | +10 | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-11 00:06 | +5 | NEAR | UP | 0.54 | 0.66 | 0.86 |
| 11-11 00:05 | +10 stop | ETH | UP | 0.57 | open |  |
| 11-11 00:05 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-11 00:05 | +10 stop | HYPE | UP | 0.51 | 0.62 | 0.75 |
| 11-11 00:04 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-11 00:04 | +5 | BNB | DOWN | 0.65 | open |  |
| 11-11 00:04 | +10 stop | HYPE | DOWN | 0.51 | 0.35 | -1.95 |
| 11-11 00:03 | +5 | ZEC | DOWN | 0.67 | open |  |
| 11-11 00:03 | +5 | SOL | UP | 0.64 | 0.82 | 1.52 |
| 11-11 00:03 | +5 | NEAR | UP | 0.62 | 0.70 | 0.48 |
| 11-11 00:03 | +10 stop | SOL | UP | 0.62 | 0.82 | 1.72 |
| 11-11 00:03 | +10 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 11-11 00:03 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 11-11 00:03 | +10 stop | HYPE | UP | 0.65 | 0.45 | -2.34 |
| 11-11 00:03 | +20 | HYPE | UP | 0.65 | open |  |
| 11-11 00:03 | +15 | HYPE | UP | 0.65 | open |  |
| 11-11 00:03 | +10 | HYPE | UP | 0.65 | open |  |
| 11-11 00:03 | +5 | HYPE | UP | 0.65 | open |  |
| 11-11 00:02 | +10 stop | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-11 00:02 | +20 | NEAR | UP | 0.67 | open |  |
| 11-11 00:02 | +15 | NEAR | UP | 0.67 | open |  |
| 11-11 00:02 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-11 00:02 | +5 | NEAR | UP | 0.67 | 0.72 | 0.19 |
| 11-11 00:02 | +10 stop | XRP | UP | 0.67 | 0.90 | 2.09 |
| 11-11 00:02 | +20 | XRP | UP | 0.67 | 0.90 | 2.09 |
| 11-11 00:02 | +15 | XRP | UP | 0.68 | 0.90 | 1.99 |
| 11-11 00:02 | +10 | XRP | UP | 0.65 | 0.90 | 2.29 |
| 11-11 00:02 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 11-11 00:02 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-11 00:01 | +10 stop | SOL | UP | 0.56 | 0.70 | 1.07 |
| 11-11 00:01 | +20 | SOL | UP | 0.56 | 0.82 | 2.31 |
| 11-11 00:01 | +15 | SOL | UP | 0.56 | 0.82 | 2.31 |
| 11-11 00:01 | +10 | SOL | UP | 0.56 | 0.70 | 1.07 |
| 11-11 00:01 | +5 | SOL | UP | 0.56 | 0.62 | 0.25 |
| 11-11 00:01 | +10 stop | BTC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-11 00:01 | +20 | BTC | DOWN | 0.68 | open |  |
| 11-11 00:01 | +15 | BTC | DOWN | 0.68 | open |  |
