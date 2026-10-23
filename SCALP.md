# Range-Scalp Bot

*Updated Fri Oct 23 03:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29702 | 25850 | 3852 (39) | 2 | $-8798.48 | -4.7% |
| **+10¢** | 22270 | 17810 | 4460 (55) | 3 | $-7934.73 | -5.7% |
| **+15¢** | 18650 | 13862 | 4788 (78) | 4 | $-7110.40 | -6.1% |
| **+20¢** | 16502 | 11485 | 5017 (100) | 8 | $-6441.96 | -6.2% |
| **+10¢ (15¢ stop)** | 36443 | 36384 | 59 (32) | 3 | $-13728.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 03:34 | +15 | ETH | UP | 0.67 | open |  |
| 10-23 03:34 | +5 | ETH | UP | 0.67 | open |  |
| 10-23 03:34 | +10 stop | XRP | UP | 0.71 | open |  |
| 10-23 03:33 | +10 | XRP | UP | 0.70 | open |  |
| 10-23 03:33 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 10-23 03:33 | +10 stop | ETH | UP | 0.64 | open |  |
| 10-23 03:33 | +10 | ETH | UP | 0.63 | open |  |
| 10-23 03:33 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 10-23 03:33 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-23 03:33 | +5 | DOGE | DOWN | 0.55 | open |  |
| 10-23 03:32 | +10 stop | HYPE | UP | 0.54 | 0.70 | 1.23 |
| 10-23 03:32 | +20 | HYPE | UP | 0.54 | open |  |
| 10-23 03:32 | +15 | HYPE | UP | 0.54 | 0.70 | 1.23 |
| 10-23 03:32 | +10 | HYPE | UP | 0.54 | 0.70 | 1.23 |
| 10-23 03:32 | +5 | HYPE | UP | 0.54 | 0.60 | 0.21 |
| 10-23 03:32 | +10 stop | SOL | UP | 0.62 | 0.73 | 0.77 |
| 10-23 03:32 | +20 | SOL | UP | 0.62 | open |  |
| 10-23 03:32 | +15 | SOL | UP | 0.62 | open |  |
| 10-23 03:32 | +10 | SOL | UP | 0.62 | 0.73 | 0.79 |
| 10-23 03:32 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 10-23 03:32 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.08 |
| 10-23 03:32 | +20 | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 10-23 03:32 | +15 | ZEC | UP | 0.58 | 0.75 | 1.39 |
| 10-23 03:32 | +10 | ZEC | UP | 0.58 | 0.72 | 1.08 |
| 10-23 03:32 | +5 | ZEC | UP | 0.58 | 0.66 | 0.49 |
| 10-23 03:32 | +5 | BTC | UP | 0.58 | 0.72 | 1.07 |
| 10-23 03:32 | +10 stop | XRP | UP | 0.57 | 0.68 | 0.76 |
| 10-23 03:32 | +20 | XRP | UP | 0.56 | open |  |
| 10-23 03:32 | +15 | XRP | UP | 0.56 | 0.71 | 1.17 |
| 10-23 03:32 | +10 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-23 03:32 | +5 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 10-23 03:32 | +10 stop | ETH | UP | 0.51 | 0.65 | 1.06 |
| 10-23 03:32 | +20 | ETH | UP | 0.51 | open |  |
| 10-23 03:32 | +15 | ETH | UP | 0.51 | 0.68 | 1.36 |
| 10-23 03:32 | +10 | ETH | UP | 0.51 | 0.65 | 1.06 |
| 10-23 03:32 | +5 | ETH | UP | 0.51 | 0.65 | 1.06 |
| 10-23 03:32 | +10 stop | NEAR | UP | 0.61 | 0.74 | 0.99 |
| 10-23 03:32 | +20 | NEAR | UP | 0.63 | open |  |
| 10-23 03:32 | +15 | NEAR | UP | 0.63 | 0.78 | 1.20 |
| 10-23 03:32 | +10 | NEAR | UP | 0.63 | 0.74 | 0.79 |
