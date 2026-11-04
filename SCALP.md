# Range-Scalp Bot

*Updated Wed Nov 04 09:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47040 | 40964 | 6076 (72) | 1 | $-13540.04 | -4.6% |
| **+10¢** | 35136 | 28091 | 7045 (97) | 4 | $-12350.74 | -5.6% |
| **+15¢** | 29421 | 21839 | 7582 (125) | 7 | $-11304.10 | -6.1% |
| **+20¢** | 26135 | 18193 | 7942 (165) | 8 | $-9973.04 | -6.1% |
| **+10¢ (15¢ stop)** | 57324 | 57231 | 93 (56) | 0 | $-21364.63 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 09:18 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 09:18 | +5 | NEAR | UP | 0.57 | open |  |
| 11-04 09:18 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-04 09:18 | +5 | XRP | DOWN | 0.60 | 0.67 | 0.37 |
| 11-04 09:17 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:17 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:17 | +10 stop | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-04 09:17 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-04 09:17 | +10 stop | NEAR | UP | 0.53 | 0.31 | -2.53 |
| 11-04 09:17 | +20 | NEAR | UP | 0.53 | open |  |
| 11-04 09:17 | +15 | NEAR | UP | 0.53 | open |  |
| 11-04 09:17 | +10 | NEAR | UP | 0.53 | open |  |
| 11-04 09:17 | +5 | NEAR | UP | 0.53 | 0.59 | 0.25 |
| 11-04 09:16 | +10 stop | BNB | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 09:16 | +15 | BNB | DOWN | 0.71 | 0.86 | 1.26 |
| 11-04 09:16 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 09:16 | +10 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-04 09:16 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-04 09:16 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-04 09:16 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-04 09:16 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:16 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 09:16 | +5 | BTC | DOWN | 0.64 | 0.73 | 0.59 |
| 11-04 09:16 | +10 stop | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-04 09:16 | +10 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 11-04 09:16 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 11-04 09:16 | +10 stop | SOL | DOWN | 0.60 | 0.72 | 0.88 |
| 11-04 09:16 | +20 | SOL | DOWN | 0.60 | 0.82 | 1.92 |
| 11-04 09:16 | +15 | SOL | DOWN | 0.60 | 0.82 | 1.92 |
| 11-04 09:16 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-04 09:16 | +5 | SOL | DOWN | 0.59 | 0.66 | 0.37 |
| 11-04 09:16 | +5 | ZEC | UP | 0.52 | 0.60 | 0.46 |
| 11-04 09:16 | +10 stop | ZEC | UP | 0.60 | 0.45 | -1.85 |
| 11-04 09:16 | +20 | ZEC | UP | 0.60 | open |  |
| 11-04 09:16 | +15 | ZEC | UP | 0.60 | open |  |
| 11-04 09:16 | +10 | ZEC | UP | 0.60 | open |  |
| 11-04 09:16 | +5 | ZEC | UP | 0.60 | 0.65 | 0.17 |
| 11-04 09:16 | +10 stop | DOGE | UP | 0.50 | 0.61 | 0.75 |
| 11-04 09:16 | +20 | DOGE | UP | 0.50 | open |  |
| 11-04 09:16 | +15 | DOGE | UP | 0.52 | open |  |
