# Range-Scalp Bot

*Updated Wed Oct 28 18:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38305 | 33426 | 4879 (46) | 3 | $-10773.67 | -4.5% |
| **+10¢** | 28576 | 22939 | 5637 (68) | 2 | $-9558.87 | -5.3% |
| **+15¢** | 23907 | 17856 | 6051 (93) | 4 | $-8485.65 | -5.7% |
| **+20¢** | 21209 | 14871 | 6338 (118) | 5 | $-7444.76 | -5.6% |
| **+10¢ (15¢ stop)** | 46868 | 46801 | 67 (35) | 0 | $-17772.61 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 18:12 | +10 stop | ETH | DOWN | 0.53 | 0.33 | -2.34 |
| 10-28 18:12 | +10 | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 10-28 18:12 | +5 | ETH | DOWN | 0.53 | 0.66 | 0.96 |
| 10-28 18:11 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.14 |
| 10-28 18:09 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-28 18:09 | +5 | ETH | DOWN | 0.67 | 0.73 | 0.30 |
| 10-28 18:09 | +10 stop | DOGE | DOWN | 0.44 | 0.55 | 0.74 |
| 10-28 18:09 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 18:09 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 18:09 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 10-28 18:08 | +10 stop | ZEC | UP | 0.58 | 0.43 | -1.86 |
| 10-28 18:08 | +10 | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 10-28 18:08 | +5 | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 10-28 18:08 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.79 |
| 10-28 18:07 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-28 18:07 | +15 | BNB | DOWN | 0.69 | 0.86 | 1.46 |
| 10-28 18:07 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-28 18:07 | +10 stop | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 10-28 18:07 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 18:07 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-28 18:07 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-28 18:07 | +10 stop | DOGE | UP | 0.59 | 0.43 | -1.95 |
| 10-28 18:07 | +20 | DOGE | UP | 0.59 | open |  |
| 10-28 18:07 | +15 | DOGE | UP | 0.59 | open |  |
| 10-28 18:07 | +10 | DOGE | UP | 0.59 | open |  |
| 10-28 18:07 | +5 | DOGE | UP | 0.59 | open |  |
| 10-28 18:07 | +10 stop | ETH | UP | 0.46 | 0.57 | 0.74 |
| 10-28 18:07 | +15 | ETH | UP | 0.46 | 0.66 | 1.66 |
| 10-28 18:07 | +10 | ETH | UP | 0.46 | 0.57 | 0.74 |
| 10-28 18:07 | +5 | ETH | UP | 0.46 | 0.57 | 0.74 |
| 10-28 18:07 | +10 stop | SOL | UP | 0.55 | 0.66 | 0.76 |
| 10-28 18:07 | +20 | SOL | UP | 0.55 | open |  |
| 10-28 18:07 | +15 | SOL | UP | 0.55 | open |  |
| 10-28 18:07 | +10 | SOL | UP | 0.55 | 0.66 | 0.76 |
| 10-28 18:07 | +5 | SOL | UP | 0.55 | 0.66 | 0.76 |
| 10-28 18:06 | +10 stop | BNB | UP | 0.62 | 0.34 | -3.13 |
| 10-28 18:06 | +5 | BNB | UP | 0.62 | open |  |
| 10-28 18:06 | +10 stop | BTC | UP | 0.62 | 0.37 | -2.84 |
| 10-28 18:06 | +20 | BTC | UP | 0.62 | open |  |
| 10-28 18:06 | +15 | BTC | UP | 0.62 | open |  |
