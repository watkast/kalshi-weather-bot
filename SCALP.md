# Range-Scalp Bot

*Updated Wed Oct 07 09:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6212 | 5393 | 819 (9) | 3 | $-1862.97 | -4.8% |
| **+10¢** | 4735 | 3771 | 964 (16) | 4 | $-1746.97 | -5.9% |
| **+15¢** | 3977 | 2957 | 1020 (20) | 4 | $-1480.17 | -5.9% |
| **+20¢** | 3559 | 2494 | 1065 (27) | 4 | $-1191.61 | -5.3% |
| **+10¢ (15¢ stop)** | 7529 | 7514 | 15 (9) | 2 | $-2605.14 | -5.5% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 09:46 | +10 stop | ZEC | UP | 0.52 | 0.62 | 0.65 |
| 10-07 09:46 | +20 | ZEC | UP | 0.52 | open |  |
| 10-07 09:46 | +15 | ZEC | UP | 0.53 | open |  |
| 10-07 09:46 | +10 | ZEC | UP | 0.53 | open |  |
| 10-07 09:46 | +5 | ZEC | UP | 0.53 | 0.62 | 0.55 |
| 10-07 09:46 | +10 stop | NEAR | UP | 0.56 | 0.34 | -2.54 |
| 10-07 09:46 | +20 | NEAR | UP | 0.56 | open |  |
| 10-07 09:46 | +15 | NEAR | UP | 0.56 | open |  |
| 10-07 09:46 | +10 | NEAR | UP | 0.56 | open |  |
| 10-07 09:46 | +5 | NEAR | UP | 0.56 | open |  |
| 10-07 09:45 | +10 stop | SOL | UP | 0.67 | open |  |
| 10-07 09:45 | +20 | SOL | UP | 0.67 | open |  |
| 10-07 09:45 | +15 | SOL | UP | 0.67 | open |  |
| 10-07 09:45 | +10 | SOL | UP | 0.67 | open |  |
| 10-07 09:45 | +5 | SOL | UP | 0.67 | open |  |
| 10-07 09:45 | +10 stop | ETH | UP | 0.59 | open |  |
| 10-07 09:45 | +20 | ETH | UP | 0.59 | open |  |
| 10-07 09:45 | +15 | ETH | UP | 0.59 | open |  |
| 10-07 09:45 | +10 | ETH | UP | 0.59 | open |  |
| 10-07 09:45 | +5 | ETH | UP | 0.59 | open |  |
| 10-07 09:38 | +10 stop | ZEC | UP | 0.59 | 0.37 | -2.54 |
| 10-07 09:34 | +10 stop | ZEC | DOWN | 0.66 | 0.38 | -3.13 |
| 10-07 09:33 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 10-07 09:33 | +15 | NEAR | DOWN | 0.71 | 0.92 | 1.89 |
| 10-07 09:33 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 10-07 09:33 | +10 stop | BTC | DOWN | 0.67 | 0.83 | 1.34 |
| 10-07 09:33 | +10 stop | ZEC | DOWN | 0.46 | 0.60 | 1.05 |
| 10-07 09:32 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.95 |
| 10-07 09:32 | +10 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 10-07 09:32 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.87 |
| 10-07 09:32 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.87 |
| 10-07 09:32 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-07 09:32 | +5 | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 10-07 09:32 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 09:32 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.86 |
| 10-07 09:32 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 10-07 09:32 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 09:32 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-07 09:31 | +10 stop | BNB | DOWN | 0.60 | 0.72 | 0.88 |
| 10-07 09:31 | +20 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
