# Range-Scalp Bot

*Updated Sat Oct 24 05:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31536 | 27490 | 4046 (40) | 8 | $-9053.05 | -4.6% |
| **+10¢** | 23576 | 18903 | 4673 (58) | 8 | $-8037.62 | -5.4% |
| **+15¢** | 19739 | 14715 | 5024 (81) | 8 | $-7179.43 | -5.8% |
| **+20¢** | 17488 | 12228 | 5260 (103) | 8 | $-6375.24 | -5.8% |
| **+10¢ (15¢ stop)** | 38703 | 38644 | 59 (32) | 6 | $-14780.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 05:55 | +10 stop | DOGE | UP | 0.59 | open |  |
| 10-24 05:55 | +15 | DOGE | UP | 0.59 | open |  |
| 10-24 05:55 | +10 | DOGE | UP | 0.59 | open |  |
| 10-24 05:55 | +10 stop | HYPE | DOWN | 0.68 | open |  |
| 10-24 05:55 | +10 stop | ETH | DOWN | 0.49 | open |  |
| 10-24 05:54 | +20 | DOGE | UP | 0.71 | open |  |
| 10-24 05:54 | +10 stop | HYPE | DOWN | 0.50 | 0.68 | 1.46 |
| 10-24 05:54 | +15 | DOGE | UP | 0.65 | 0.86 | 1.81 |
| 10-24 05:54 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-24 05:53 | +10 stop | NEAR | UP | 0.56 | open |  |
| 10-24 05:53 | +10 stop | XRP | DOWN | 0.68 | 0.86 | 1.55 |
| 10-24 05:53 | +10 stop | DOGE | UP | 0.60 | 0.86 | 2.29 |
| 10-24 05:53 | +10 | DOGE | UP | 0.60 | 0.86 | 2.29 |
| 10-24 05:53 | +10 stop | SOL | UP | 0.59 | open |  |
| 10-24 05:52 | +5 | SOL | DOWN | 0.56 | open |  |
| 10-24 05:52 | +5 | DOGE | DOWN | 0.66 | open |  |
| 10-24 05:52 | +10 stop | ETH | DOWN | 0.71 | 0.51 | -2.33 |
| 10-24 05:52 | +10 stop | SOL | DOWN | 0.55 | 0.38 | -2.05 |
| 10-24 05:52 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-24 05:52 | +10 stop | NEAR | DOWN | 0.67 | 0.35 | -3.52 |
| 10-24 05:51 | +10 stop | SOL | UP | 0.43 | 0.55 | 0.84 |
| 10-24 05:51 | +5 | ETH | UP | 0.34 | 0.57 | 1.96 |
| 10-24 05:51 | +10 stop | BTC | UP | 0.51 | 0.64 | 0.95 |
| 10-24 05:50 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.90 |
| 10-24 05:50 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-24 05:50 | +10 | NEAR | DOWN | 0.68 | open |  |
| 10-24 05:50 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-24 05:50 | +10 stop | BNB | DOWN | 0.68 | 0.81 | 1.03 |
| 10-24 05:50 | +5 | SOL | DOWN | 0.54 | 0.59 | 0.15 |
| 10-24 05:49 | +10 stop | HYPE | DOWN | 0.68 | 0.49 | -2.28 |
| 10-24 05:49 | +15 | HYPE | DOWN | 0.68 | open |  |
| 10-24 05:49 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-24 05:49 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-24 05:49 | +10 stop | DOGE | DOWN | 0.63 | 0.40 | -2.64 |
| 10-24 05:49 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 10-24 05:48 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.08 |
| 10-24 05:48 | +10 stop | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 10-24 05:48 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-24 05:48 | +5 | ETH | DOWN | 0.55 | 0.60 | 0.15 |
| 10-24 05:48 | +5 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
