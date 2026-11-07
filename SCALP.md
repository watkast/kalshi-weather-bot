# Range-Scalp Bot

*Updated Sat Nov 07 11:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50941 | 44408 | 6533 (76) | 3 | $-14281.74 | -4.5% |
| **+10¢** | 38029 | 30416 | 7613 (102) | 6 | $-13246.67 | -5.5% |
| **+15¢** | 31833 | 23630 | 8203 (131) | 6 | $-12166.56 | -6.1% |
| **+20¢** | 28307 | 19709 | 8598 (173) | 6 | $-10746.15 | -6.1% |
| **+10¢ (15¢ stop)** | 62040 | 61941 | 99 (58) | 4 | $-22926.08 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 11:34 | +10 stop | HYPE | DOWN | 0.54 | open |  |
| 11-07 11:34 | +10 stop | ETH | UP | 0.66 | open |  |
| 11-07 11:34 | +10 | ETH | UP | 0.66 | open |  |
| 11-07 11:34 | +5 | ETH | UP | 0.66 | open |  |
| 11-07 11:34 | +5 | XRP | UP | 0.69 | 0.76 | 0.42 |
| 11-07 11:34 | +5 | BNB | UP | 0.49 | 0.62 | 0.95 |
| 11-07 11:34 | +10 stop | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-07 11:34 | +10 | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-07 11:34 | +5 | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-07 11:33 | +10 stop | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-07 11:33 | +10 | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-07 11:33 | +5 | ETH | DOWN | 0.41 | 0.54 | 0.95 |
| 11-07 11:32 | +10 stop | NEAR | DOWN | 0.60 | 0.24 | -3.90 |
| 11-07 11:32 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-07 11:32 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-07 11:32 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-07 11:32 | +5 | NEAR | DOWN | 0.60 | open |  |
| 11-07 11:32 | +10 stop | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-07 11:32 | +10 | XRP | UP | 0.59 | 0.71 | 0.88 |
| 11-07 11:32 | +5 | XRP | UP | 0.59 | 0.64 | 0.16 |
| 11-07 11:31 | +10 stop | BNB | UP | 0.57 | 0.37 | -2.35 |
| 11-07 11:31 | +20 | BNB | UP | 0.57 | open |  |
| 11-07 11:31 | +15 | BNB | UP | 0.57 | open |  |
| 11-07 11:31 | +10 | BNB | UP | 0.57 | open |  |
| 11-07 11:31 | +5 | BNB | UP | 0.57 | 0.65 | 0.46 |
| 11-07 11:31 | +10 stop | SOL | UP | 0.54 | 0.76 | 1.89 |
| 11-07 11:31 | +20 | SOL | UP | 0.54 | 0.76 | 1.89 |
| 11-07 11:31 | +15 | SOL | UP | 0.54 | 0.76 | 1.89 |
| 11-07 11:31 | +10 | SOL | UP | 0.54 | 0.76 | 1.89 |
| 11-07 11:31 | +5 | SOL | UP | 0.54 | 0.61 | 0.35 |
| 11-07 11:31 | +10 stop | BTC | UP | 0.68 | open |  |
| 11-07 11:31 | +20 | BTC | UP | 0.68 | open |  |
| 11-07 11:31 | +15 | BTC | UP | 0.68 | open |  |
| 11-07 11:31 | +10 | BTC | UP | 0.68 | open |  |
| 11-07 11:31 | +5 | BTC | UP | 0.68 | 0.74 | 0.30 |
| 11-07 11:31 | +10 stop | ETH | DOWN | 0.46 | 0.58 | 0.84 |
| 11-07 11:31 | +20 | ETH | DOWN | 0.46 | open |  |
| 11-07 11:31 | +15 | ETH | DOWN | 0.46 | open |  |
| 11-07 11:31 | +10 | ETH | DOWN | 0.46 | 0.58 | 0.84 |
| 11-07 11:31 | +5 | ETH | DOWN | 0.46 | 0.58 | 0.84 |
