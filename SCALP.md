# Range-Scalp Bot

*Updated Fri Nov 20 01:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65653 | 57306 | 8347 (124) | 0 | $-17606.79 | -4.3% |
| **+10¢** | 49031 | 39271 | 9760 (165) | 2 | $-16380.37 | -5.3% |
| **+15¢** | 41119 | 30590 | 10529 (211) | 2 | $-14758.30 | -5.7% |
| **+20¢** | 36609 | 25549 | 11060 (266) | 2 | $-13067.42 | -5.7% |
| **+10¢ (15¢ stop)** | 79918 | 79754 | 164 (98) | 0 | $-29423.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 01:50 | +10 stop | DOGE | DOWN | 0.65 | 0.83 | 1.54 |
| 11-20 01:50 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-20 01:50 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.90 |
| 11-20 01:50 | +5 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 11-20 01:50 | +15 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-20 01:50 | +10 stop | BNB | DOWN | 0.58 | 0.77 | 1.59 |
| 11-20 01:50 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 11-20 01:50 | +10 stop | HYPE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-20 01:50 | +10 stop | SOL | DOWN | 0.55 | 0.69 | 1.07 |
| 11-20 01:50 | +10 stop | XRP | DOWN | 0.58 | 0.77 | 1.59 |
| 11-20 01:50 | +10 stop | ZEC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-20 01:50 | +10 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-20 01:50 | +10 stop | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 11-20 01:50 | +5 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 11-20 01:50 | +5 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-20 01:50 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-20 01:49 | +5 | ETH | UP | 0.51 | 0.59 | 0.45 |
| 11-20 01:49 | +10 stop | SOL | UP | 0.58 | 0.38 | -2.35 |
| 11-20 01:49 | +15 | SOL | UP | 0.58 | open |  |
| 11-20 01:49 | +10 | SOL | UP | 0.56 | open |  |
| 11-20 01:49 | +5 | SOL | UP | 0.55 | 0.63 | 0.45 |
| 11-20 01:49 | +10 stop | BTC | UP | 0.45 | 0.59 | 1.05 |
| 11-20 01:48 | +5 | ZEC | UP | 0.57 | 0.64 | 0.35 |
| 11-20 01:47 | +10 stop | DOGE | UP | 0.59 | 0.33 | -2.93 |
| 11-20 01:47 | +10 stop | HYPE | UP | 0.59 | 0.41 | -2.14 |
| 11-20 01:47 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 11-20 01:47 | +10 stop | XRP | UP | 0.69 | 0.45 | -2.73 |
| 11-20 01:47 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-20 01:47 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-20 01:47 | +20 | NEAR | DOWN | 0.68 | 0.90 | 2.04 |
| 11-20 01:47 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 11-20 01:47 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.25 |
| 11-20 01:47 | +5 | NEAR | DOWN | 0.67 | 0.82 | 1.25 |
| 11-20 01:47 | +10 stop | ETH | UP | 0.68 | 0.51 | -2.04 |
| 11-20 01:47 | +20 | ETH | UP | 0.68 | open |  |
| 11-20 01:47 | +15 | ETH | UP | 0.67 | open |  |
| 11-20 01:47 | +10 | ETH | UP | 0.67 | open |  |
| 11-20 01:47 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-20 01:47 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-20 01:47 | +20 | SOL | UP | 0.60 | open |  |
