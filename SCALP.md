# Range-Scalp Bot

*Updated Mon Nov 09 03:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53204 | 46397 | 6807 (85) | 7 | $-14650.89 | -4.4% |
| **+10¢** | 39727 | 31787 | 7940 (110) | 8 | $-13643.65 | -5.5% |
| **+15¢** | 33289 | 24733 | 8556 (141) | 8 | $-12453.61 | -6.0% |
| **+20¢** | 29613 | 20642 | 8971 (186) | 8 | $-10954.06 | -5.9% |
| **+10¢ (15¢ stop)** | 64818 | 64712 | 106 (63) | 0 | $-24014.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 03:06 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-09 03:06 | +10 stop | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-09 03:06 | +10 | BTC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-09 03:05 | +5 | BTC | DOWN | 0.70 | 0.87 | 1.47 |
| 11-09 03:03 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-09 03:03 | +10 stop | ETH | UP | 0.60 | 0.30 | -3.32 |
| 11-09 03:03 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-09 03:03 | +10 stop | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-09 03:03 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-09 03:03 | +20 | BTC | DOWN | 0.60 | 0.87 | 2.45 |
| 11-09 03:03 | +15 | BTC | DOWN | 0.60 | 0.87 | 2.45 |
| 11-09 03:03 | +10 | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 11-09 03:03 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-09 03:02 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 03:02 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-09 03:02 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-09 03:02 | +10 stop | DOGE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-09 03:01 | +10 stop | BNB | UP | 0.62 | 0.40 | -2.54 |
| 11-09 03:01 | +20 | BNB | UP | 0.62 | open |  |
| 11-09 03:01 | +15 | BNB | UP | 0.62 | open |  |
| 11-09 03:01 | +10 | BNB | UP | 0.62 | open |  |
| 11-09 03:01 | +5 | BNB | UP | 0.62 | open |  |
| 11-09 03:01 | +10 stop | XRP | UP | 0.60 | 0.38 | -2.54 |
| 11-09 03:01 | +20 | XRP | UP | 0.60 | open |  |
| 11-09 03:01 | +15 | XRP | UP | 0.60 | open |  |
| 11-09 03:01 | +10 | XRP | UP | 0.60 | open |  |
| 11-09 03:01 | +5 | XRP | UP | 0.60 | open |  |
| 11-09 03:01 | +10 stop | ZEC | UP | 0.68 | 0.52 | -1.94 |
| 11-09 03:01 | +20 | ZEC | UP | 0.68 | open |  |
| 11-09 03:01 | +15 | ZEC | UP | 0.68 | open |  |
| 11-09 03:01 | +10 | ZEC | UP | 0.68 | open |  |
| 11-09 03:01 | +5 | ZEC | UP | 0.68 | open |  |
| 11-09 03:01 | +10 stop | SOL | UP | 0.62 | 0.46 | -1.95 |
| 11-09 03:01 | +20 | SOL | UP | 0.62 | open |  |
| 11-09 03:01 | +15 | SOL | UP | 0.61 | open |  |
| 11-09 03:01 | +10 | SOL | UP | 0.62 | open |  |
| 11-09 03:01 | +5 | SOL | UP | 0.62 | open |  |
| 11-09 03:01 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 11-09 03:01 | +20 | ETH | UP | 0.67 | open |  |
| 11-09 03:01 | +15 | ETH | UP | 0.67 | open |  |
