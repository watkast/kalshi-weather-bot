# Range-Scalp Bot

*Updated Wed Nov 18 06:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63705 | 55562 | 8143 (118) | 4 | $-17417.36 | -4.3% |
| **+10¢** | 47593 | 38060 | 9533 (159) | 4 | $-16351.69 | -5.5% |
| **+15¢** | 39901 | 29622 | 10279 (204) | 8 | $-14825.98 | -5.9% |
| **+20¢** | 35537 | 24749 | 10788 (259) | 9 | $-13103.40 | -5.9% |
| **+10¢ (15¢ stop)** | 77508 | 77350 | 158 (93) | 1 | $-28468.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 06:08 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-18 06:08 | +10 stop | XRP | DOWN | 0.71 | open |  |
| 11-18 06:08 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-18 06:08 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-18 06:08 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-18 06:08 | +5 | XRP | DOWN | 0.71 | 0.78 | 0.42 |
| 11-18 06:07 | +10 stop | BTC | UP | 0.71 | 0.54 | -2.03 |
| 11-18 06:07 | +5 | BTC | UP | 0.71 | open |  |
| 11-18 06:07 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-18 06:07 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-18 06:07 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-18 06:07 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-18 06:07 | +5 | DOGE | DOWN | 0.58 | 0.67 | 0.56 |
| 11-18 06:07 | +10 stop | SOL | DOWN | 0.50 | 0.63 | 0.95 |
| 11-18 06:07 | +10 | SOL | DOWN | 0.51 | 0.63 | 0.85 |
| 11-18 06:07 | +5 | SOL | DOWN | 0.51 | 0.63 | 0.85 |
| 11-18 06:06 | +10 stop | ETH | DOWN | 0.55 | 0.40 | -1.85 |
| 11-18 06:05 | +5 | BNB | UP | 0.61 | 0.67 | 0.27 |
| 11-18 06:05 | +10 stop | NEAR | DOWN | 0.56 | 0.39 | -2.05 |
| 11-18 06:05 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 06:05 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-18 06:05 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-18 06:05 | +10 | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 06:05 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 11-18 06:05 | +10 stop | BNB | UP | 0.55 | 0.67 | 0.86 |
| 11-18 06:05 | +10 | BNB | UP | 0.55 | 0.67 | 0.86 |
| 11-18 06:05 | +5 | BNB | UP | 0.55 | 0.63 | 0.45 |
| 11-18 06:04 | +10 stop | BNB | UP | 0.47 | 0.57 | 0.64 |
| 11-18 06:04 | +10 | BNB | UP | 0.47 | 0.57 | 0.64 |
| 11-18 06:04 | +5 | BNB | UP | 0.47 | 0.57 | 0.64 |
| 11-18 06:03 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-18 06:03 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-18 06:03 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-18 06:03 | +10 | HYPE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-18 06:03 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.37 |
| 11-18 06:03 | +5 | ZEC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-18 06:03 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-18 06:03 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-18 06:03 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-18 06:03 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
