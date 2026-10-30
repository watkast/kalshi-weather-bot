# Range-Scalp Bot

*Updated Fri Oct 30 02:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40092 | 35023 | 5069 (51) | 6 | $-10975.94 | -4.3% |
| **+10¢** | 29870 | 24004 | 5866 (74) | 6 | $-9728.64 | -5.2% |
| **+15¢** | 24984 | 18672 | 6312 (101) | 6 | $-8711.46 | -5.6% |
| **+20¢** | 22169 | 15550 | 6619 (130) | 5 | $-7639.53 | -5.5% |
| **+10¢ (15¢ stop)** | 48906 | 48836 | 70 (37) | 4 | $-18499.26 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 02:37 | +5 | BNB | UP | 0.68 | open |  |
| 10-30 02:37 | +10 | NEAR | UP | 0.68 | open |  |
| 10-30 02:36 | +10 stop | HYPE | UP | 0.65 | 0.81 | 1.33 |
| 10-30 02:36 | +10 stop | BNB | UP | 0.53 | 0.65 | 0.86 |
| 10-30 02:36 | +20 | BNB | UP | 0.53 | open |  |
| 10-30 02:36 | +15 | BNB | UP | 0.54 | open |  |
| 10-30 02:36 | +10 | BNB | UP | 0.53 | 0.65 | 0.86 |
| 10-30 02:36 | +5 | BNB | UP | 0.53 | 0.58 | 0.14 |
| 10-30 02:36 | +10 stop | ETH | UP | 0.61 | open |  |
| 10-30 02:36 | +10 stop | SOL | UP | 0.64 | open |  |
| 10-30 02:36 | +15 | SOL | UP | 0.64 | open |  |
| 10-30 02:36 | +10 | SOL | UP | 0.62 | open |  |
| 10-30 02:36 | +5 | ETH | UP | 0.59 | open |  |
| 10-30 02:36 | +10 stop | DOGE | UP | 0.58 | 0.70 | 0.87 |
| 10-30 02:36 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-30 02:36 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 10-30 02:36 | +10 stop | XRP | UP | 0.65 | open |  |
| 10-30 02:36 | +5 | XRP | UP | 0.65 | open |  |
| 10-30 02:35 | +5 | ETH | DOWN | 0.49 | 0.58 | 0.54 |
| 10-30 02:35 | +5 | XRP | DOWN | 0.55 | 0.63 | 0.45 |
| 10-30 02:35 | +15 | HYPE | DOWN | 0.64 | open |  |
| 10-30 02:35 | +5 | HYPE | DOWN | 0.64 | open |  |
| 10-30 02:35 | +10 stop | SOL | DOWN | 0.60 | 0.36 | -2.74 |
| 10-30 02:35 | +5 | SOL | DOWN | 0.60 | open |  |
| 10-30 02:35 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-30 02:35 | +10 stop | NEAR | DOWN | 0.55 | 0.34 | -2.44 |
| 10-30 02:34 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-30 02:34 | +10 stop | BTC | DOWN | 0.66 | 0.46 | -2.34 |
| 10-30 02:34 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.30 |
| 10-30 02:34 | +5 | XRP | DOWN | 0.60 | 0.66 | 0.27 |
| 10-30 02:34 | +10 stop | DOGE | DOWN | 0.64 | 0.47 | -2.05 |
| 10-30 02:34 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-30 02:34 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-30 02:34 | +10 | DOGE | DOWN | 0.64 | open |  |
| 10-30 02:34 | +5 | DOGE | DOWN | 0.64 | open |  |
| 10-30 02:33 | +10 stop | ETH | DOWN | 0.60 | 0.41 | -2.24 |
| 10-30 02:33 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-30 02:33 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-30 02:33 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-30 02:33 | +5 | ETH | DOWN | 0.60 | 0.69 | 0.58 |
