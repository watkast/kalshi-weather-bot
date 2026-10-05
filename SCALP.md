# Range-Scalp Bot

*Updated Mon Oct 05 02:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3114 | 2669 | 445 (3) | 4 | $-1156.66 | -5.9% |
| **+10¢** | 2414 | 1908 | 506 (4) | 4 | $-1027.84 | -6.8% |
| **+15¢** | 2030 | 1496 | 534 (5) | 8 | $-909.56 | -7.1% |
| **+20¢** | 1810 | 1255 | 555 (10) | 9 | $-768.98 | -6.8% |
| **+10¢ (15¢ stop)** | 3884 | 3883 | 1 (1) | 4 | $-1537.42 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 02:03 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-05 02:02 | +5 | DOGE | UP | 0.59 | 0.68 | 0.59 |
| 10-05 02:02 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 10-05 02:02 | +5 | ZEC | UP | 0.62 | 0.70 | 0.52 |
| 10-05 02:02 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 10-05 02:02 | +20 | HYPE | DOWN | 0.56 | open |  |
| 10-05 02:02 | +15 | HYPE | DOWN | 0.56 | open |  |
| 10-05 02:02 | +10 | HYPE | DOWN | 0.56 | open |  |
| 10-05 02:02 | +5 | HYPE | DOWN | 0.56 | open |  |
| 10-05 02:02 | +10 stop | NEAR | UP | 0.57 | open |  |
| 10-05 02:02 | +20 | NEAR | UP | 0.57 | open |  |
| 10-05 02:02 | +15 | NEAR | UP | 0.57 | open |  |
| 10-05 02:02 | +10 | NEAR | UP | 0.57 | open |  |
| 10-05 02:02 | +5 | NEAR | UP | 0.57 | open |  |
| 10-05 02:02 | +10 stop | ETH | UP | 0.70 | open |  |
| 10-05 02:02 | +20 | ETH | UP | 0.70 | open |  |
| 10-05 02:02 | +15 | ETH | UP | 0.70 | open |  |
| 10-05 02:02 | +10 | ETH | UP | 0.70 | open |  |
| 10-05 02:02 | +5 | ETH | UP | 0.70 | open |  |
| 10-05 02:01 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-05 02:01 | +20 | DOGE | UP | 0.55 | open |  |
| 10-05 02:01 | +15 | DOGE | UP | 0.55 | open |  |
| 10-05 02:01 | +10 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 10-05 02:01 | +5 | DOGE | UP | 0.55 | 0.61 | 0.25 |
| 10-05 02:01 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 10-05 02:01 | +20 | XRP | UP | 0.59 | open |  |
| 10-05 02:01 | +15 | XRP | UP | 0.59 | open |  |
| 10-05 02:01 | +10 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-05 02:01 | +5 | XRP | UP | 0.58 | 0.65 | 0.36 |
| 10-05 02:01 | +10 stop | BNB | UP | 0.63 | 0.79 | 1.31 |
| 10-05 02:01 | +20 | BNB | UP | 0.63 | open |  |
| 10-05 02:01 | +15 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 10-05 02:01 | +10 | BNB | UP | 0.63 | 0.79 | 1.31 |
| 10-05 02:01 | +5 | BNB | UP | 0.63 | 0.71 | 0.48 |
| 10-05 02:01 | +10 stop | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-05 02:01 | +20 | SOL | UP | 0.62 | open |  |
| 10-05 02:01 | +15 | SOL | UP | 0.62 | open |  |
| 10-05 02:01 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-05 02:01 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 10-05 02:01 | +10 stop | BTC | UP | 0.52 | open |  |
