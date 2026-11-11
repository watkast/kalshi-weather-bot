# Range-Scalp Bot

*Updated Wed Nov 11 23:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56338 | 49126 | 7212 (95) | 7 | $-15438.69 | -4.4% |
| **+10¢** | 42095 | 33680 | 8415 (125) | 8 | $-14401.26 | -5.4% |
| **+15¢** | 35297 | 26229 | 9068 (159) | 9 | $-13090.16 | -5.9% |
| **+20¢** | 31445 | 21931 | 9514 (209) | 9 | $-11448.92 | -5.8% |
| **+10¢ (15¢ stop)** | 68662 | 68541 | 121 (73) | 0 | $-25324.39 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 23:07 | +5 | NEAR | UP | 0.43 | 0.54 | 0.74 |
| 11-11 23:07 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-11 23:07 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.75 |
| 11-11 23:07 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-11 23:07 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-11 23:06 | +10 stop | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-11 23:06 | +10 | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-11 23:06 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-11 23:06 | +10 stop | NEAR | UP | 0.50 | 0.20 | -3.30 |
| 11-11 23:06 | +20 | NEAR | UP | 0.50 | open |  |
| 11-11 23:06 | +15 | NEAR | UP | 0.50 | open |  |
| 11-11 23:06 | +10 | NEAR | UP | 0.50 | open |  |
| 11-11 23:06 | +5 | NEAR | UP | 0.50 | 0.58 | 0.44 |
| 11-11 23:06 | +10 stop | BNB | UP | 0.64 | 0.43 | -2.45 |
| 11-11 23:06 | +15 | BNB | UP | 0.67 | open |  |
| 11-11 23:06 | +10 | BNB | UP | 0.67 | open |  |
| 11-11 23:06 | +5 | BNB | UP | 0.67 | open |  |
| 11-11 23:06 | +10 stop | BTC | UP | 0.65 | 0.48 | -2.04 |
| 11-11 23:06 | +20 | BTC | UP | 0.65 | open |  |
| 11-11 23:06 | +15 | BTC | UP | 0.65 | open |  |
| 11-11 23:06 | +10 | BTC | UP | 0.65 | open |  |
| 11-11 23:06 | +5 | BTC | UP | 0.65 | open |  |
| 11-11 23:06 | +10 stop | DOGE | UP | 0.64 | 0.32 | -3.53 |
| 11-11 23:06 | +20 | DOGE | UP | 0.64 | open |  |
| 11-11 23:06 | +15 | DOGE | UP | 0.64 | open |  |
| 11-11 23:06 | +10 | DOGE | UP | 0.64 | open |  |
| 11-11 23:06 | +5 | DOGE | UP | 0.64 | open |  |
| 11-11 23:06 | +10 stop | ETH | UP | 0.57 | 0.33 | -2.77 |
| 11-11 23:06 | +10 | ETH | UP | 0.57 | open |  |
| 11-11 23:06 | +5 | ETH | UP | 0.57 | open |  |
| 11-11 23:05 | +5 | ZEC | UP | 0.65 | open |  |
| 11-11 23:05 | +10 stop | XRP | UP | 0.64 | 0.35 | -3.22 |
| 11-11 23:05 | +15 | XRP | UP | 0.64 | open |  |
| 11-11 23:05 | +10 | XRP | UP | 0.63 | open |  |
| 11-11 23:05 | +5 | XRP | UP | 0.63 | open |  |
| 11-11 23:04 | +10 stop | SOL | UP | 0.60 | 0.45 | -1.85 |
| 11-11 23:04 | +20 | SOL | UP | 0.61 | open |  |
| 11-11 23:04 | +15 | SOL | UP | 0.61 | open |  |
| 11-11 23:04 | +10 | SOL | UP | 0.61 | open |  |
| 11-11 23:04 | +5 | SOL | UP | 0.61 | open |  |
