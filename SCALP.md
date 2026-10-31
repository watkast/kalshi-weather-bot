# Range-Scalp Bot

*Updated Sat Oct 31 18:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42583 | 37132 | 5451 (59) | 5 | $-12054.65 | -4.5% |
| **+10¢** | 31752 | 25444 | 6308 (81) | 5 | $-10840.65 | -5.4% |
| **+15¢** | 26558 | 19755 | 6803 (109) | 6 | $-9951.54 | -6.0% |
| **+20¢** | 23587 | 16455 | 7132 (141) | 7 | $-8845.36 | -6.0% |
| **+10¢ (15¢ stop)** | 51961 | 51882 | 79 (44) | 1 | $-19687.86 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 18:21 | +10 stop | BNB | UP | 0.41 | 0.54 | 0.95 |
| 10-31 18:19 | +10 stop | BTC | UP | 0.58 | 0.71 | 0.97 |
| 10-31 18:19 | +10 stop | DOGE | UP | 0.69 | open |  |
| 10-31 18:19 | +20 | DOGE | UP | 0.69 | open |  |
| 10-31 18:19 | +15 | DOGE | UP | 0.69 | open |  |
| 10-31 18:19 | +10 | DOGE | UP | 0.69 | open |  |
| 10-31 18:19 | +5 | DOGE | UP | 0.70 | open |  |
| 10-31 18:19 | +10 stop | BNB | DOWN | 0.59 | 0.44 | -1.85 |
| 10-31 18:19 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 10-31 18:18 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 10-31 18:18 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-31 18:18 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-31 18:18 | +10 | ETH | DOWN | 0.62 | open |  |
| 10-31 18:18 | +5 | ETH | DOWN | 0.62 | open |  |
| 10-31 18:16 | +10 stop | BTC | UP | 0.70 | 0.55 | -1.83 |
| 10-31 18:16 | +20 | BTC | UP | 0.70 | open |  |
| 10-31 18:16 | +15 | BTC | UP | 0.70 | open |  |
| 10-31 18:16 | +10 | BTC | UP | 0.70 | open |  |
| 10-31 18:16 | +5 | BTC | UP | 0.69 | open |  |
| 10-31 18:16 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 10-31 18:16 | +20 | ZEC | UP | 0.69 | open |  |
| 10-31 18:16 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 10-31 18:16 | +10 | ZEC | UP | 0.65 | 0.75 | 0.70 |
| 10-31 18:16 | +5 | ZEC | UP | 0.65 | 0.70 | 0.19 |
| 10-31 18:16 | +10 stop | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 10-31 18:16 | +20 | NEAR | UP | 0.70 | 0.90 | 1.82 |
| 10-31 18:16 | +15 | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 10-31 18:16 | +10 | NEAR | UP | 0.70 | 0.89 | 1.68 |
| 10-31 18:16 | +5 | NEAR | UP | 0.70 | 0.76 | 0.32 |
| 10-31 18:16 | +5 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-31 18:16 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.90 |
| 10-31 18:16 | +20 | BNB | UP | 0.59 | open |  |
| 10-31 18:16 | +15 | BNB | UP | 0.59 | open |  |
| 10-31 18:16 | +10 | BNB | UP | 0.59 | open |  |
| 10-31 18:16 | +5 | BNB | UP | 0.60 | open |  |
| 10-31 18:15 | +10 stop | SOL | UP | 0.61 | 0.74 | 0.99 |
| 10-31 18:15 | +20 | SOL | UP | 0.61 | open |  |
| 10-31 18:15 | +15 | SOL | UP | 0.61 | open |  |
| 10-31 18:15 | +10 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 10-31 18:15 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
