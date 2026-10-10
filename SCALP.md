# Range-Scalp Bot

*Updated Sat Oct 10 17:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10681 | 9204 | 1477 (22) | 2 | $-3671.15 | -5.4% |
| **+10¢** | 8088 | 6369 | 1719 (36) | 4 | $-3494.77 | -6.9% |
| **+15¢** | 6826 | 5007 | 1819 (52) | 4 | $-2949.27 | -6.9% |
| **+20¢** | 6071 | 4175 | 1896 (66) | 4 | $-2516.44 | -6.6% |
| **+10¢ (15¢ stop)** | 13135 | 13094 | 41 (25) | 1 | $-5229.60 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 17:59 | +10 stop | DOGE | UP | 0.69 | open |  |
| 10-10 17:59 | +20 | DOGE | UP | 0.69 | open |  |
| 10-10 17:59 | +15 | DOGE | UP | 0.69 | open |  |
| 10-10 17:59 | +10 | DOGE | UP | 0.69 | open |  |
| 10-10 17:59 | +5 | DOGE | UP | 0.69 | open |  |
| 10-10 17:58 | +10 stop | ZEC | DOWN | 0.70 | 0.95 | 2.30 |
| 10-10 17:58 | +10 | ZEC | DOWN | 0.70 | 0.95 | 2.30 |
| 10-10 17:58 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 10-10 17:57 | +10 stop | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-10 17:57 | +20 | ZEC | DOWN | 0.46 | 0.70 | 2.07 |
| 10-10 17:57 | +15 | ZEC | DOWN | 0.46 | 0.70 | 2.07 |
| 10-10 17:57 | +10 | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-10 17:57 | +5 | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-10 17:56 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 10-10 17:56 | +10 stop | DOGE | UP | 0.54 | 0.33 | -2.44 |
| 10-10 17:56 | +20 | DOGE | UP | 0.54 | 0.77 | 1.99 |
| 10-10 17:56 | +15 | DOGE | UP | 0.54 | 0.77 | 1.99 |
| 10-10 17:56 | +10 | DOGE | UP | 0.54 | 0.64 | 0.65 |
| 10-10 17:56 | +5 | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-10 17:56 | +10 stop | ETH | DOWN | 0.58 | 0.71 | 0.97 |
| 10-10 17:56 | +5 | SOL | DOWN | 0.65 | 0.86 | 1.85 |
| 10-10 17:56 | +10 stop | XRP | UP | 0.49 | 0.32 | -2.04 |
| 10-10 17:56 | +10 | XRP | UP | 0.49 | open |  |
| 10-10 17:56 | +5 | XRP | UP | 0.49 | 0.54 | 0.14 |
| 10-10 17:55 | +5 | SOL | UP | 0.44 | 0.55 | 0.74 |
| 10-10 17:54 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.70 |
| 10-10 17:54 | +20 | NEAR | DOWN | 0.61 | 0.84 | 2.05 |
| 10-10 17:54 | +15 | NEAR | DOWN | 0.61 | 0.78 | 1.40 |
| 10-10 17:54 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-10 17:54 | +5 | NEAR | DOWN | 0.61 | 0.71 | 0.69 |
| 10-10 17:54 | +10 stop | ETH | DOWN | 0.64 | 0.45 | -2.24 |
| 10-10 17:54 | +10 stop | SOL | UP | 0.55 | 0.32 | -2.64 |
| 10-10 17:54 | +20 | SOL | UP | 0.54 | open |  |
| 10-10 17:54 | +15 | SOL | UP | 0.54 | open |  |
| 10-10 17:54 | +10 | SOL | UP | 0.54 | open |  |
| 10-10 17:54 | +5 | SOL | UP | 0.54 | 0.62 | 0.45 |
| 10-10 17:53 | +5 | XRP | UP | 0.64 | 0.77 | 1.02 |
| 10-10 17:53 | +10 stop | XRP | UP | 0.64 | 0.42 | -2.55 |
| 10-10 17:53 | +10 stop | BTC | UP | 0.63 | 0.32 | -3.43 |
| 10-10 17:53 | +20 | ETH | DOWN | 0.52 | 0.76 | 2.09 |
