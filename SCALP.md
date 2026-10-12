# Range-Scalp Bot

*Updated Mon Oct 12 04:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13038 | 11256 | 1782 (25) | 7 | $-4308.44 | -5.2% |
| **+10¢** | 9885 | 7826 | 2059 (37) | 7 | $-4013.31 | -6.4% |
| **+15¢** | 8311 | 6112 | 2199 (55) | 7 | $-3535.34 | -6.8% |
| **+20¢** | 7401 | 5109 | 2292 (69) | 7 | $-3028.41 | -6.5% |
| **+10¢ (15¢ stop)** | 16070 | 16029 | 41 (25) | 6 | $-6347.01 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 04:17 | +10 stop | DOGE | UP | 0.54 | open |  |
| 10-12 04:17 | +20 | DOGE | UP | 0.54 | open |  |
| 10-12 04:17 | +15 | DOGE | UP | 0.54 | open |  |
| 10-12 04:17 | +10 | DOGE | UP | 0.54 | open |  |
| 10-12 04:17 | +5 | DOGE | UP | 0.54 | open |  |
| 10-12 04:17 | +5 | ETH | DOWN | 0.67 | open |  |
| 10-12 04:16 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 10-12 04:16 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-12 04:16 | +15 | BTC | DOWN | 0.59 | open |  |
| 10-12 04:16 | +10 | BTC | DOWN | 0.59 | open |  |
| 10-12 04:16 | +5 | BTC | DOWN | 0.59 | open |  |
| 10-12 04:16 | +10 stop | SOL | DOWN | 0.61 | open |  |
| 10-12 04:16 | +20 | SOL | DOWN | 0.61 | open |  |
| 10-12 04:16 | +15 | SOL | DOWN | 0.61 | open |  |
| 10-12 04:16 | +10 | SOL | DOWN | 0.61 | open |  |
| 10-12 04:16 | +5 | SOL | DOWN | 0.61 | open |  |
| 10-12 04:16 | +10 stop | BNB | UP | 0.59 | open |  |
| 10-12 04:16 | +20 | BNB | UP | 0.59 | open |  |
| 10-12 04:16 | +15 | BNB | UP | 0.59 | open |  |
| 10-12 04:16 | +10 | BNB | UP | 0.59 | open |  |
| 10-12 04:16 | +5 | BNB | UP | 0.59 | open |  |
| 10-12 04:16 | +10 stop | ZEC | DOWN | 0.62 | 0.36 | -2.91 |
| 10-12 04:16 | +20 | ZEC | DOWN | 0.61 | open |  |
| 10-12 04:16 | +15 | ZEC | DOWN | 0.61 | open |  |
| 10-12 04:16 | +10 | ZEC | DOWN | 0.61 | open |  |
| 10-12 04:16 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-12 04:16 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-12 04:16 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-12 04:16 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-12 04:16 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-12 04:16 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-12 04:16 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 10-12 04:16 | +20 | ETH | DOWN | 0.60 | open |  |
| 10-12 04:16 | +15 | ETH | DOWN | 0.60 | open |  |
| 10-12 04:16 | +10 | ETH | DOWN | 0.60 | open |  |
| 10-12 04:16 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.22 |
| 10-12 04:10 | +10 stop | SOL | DOWN | 0.56 | 0.68 | 0.86 |
| 10-12 04:09 | +10 stop | SOL | DOWN | 0.67 | 0.48 | -2.24 |
| 10-12 04:08 | +10 stop | ZEC | DOWN | 0.65 | 0.49 | -1.94 |
| 10-12 04:05 | +10 stop | ZEC | DOWN | 0.59 | 0.42 | -2.05 |
