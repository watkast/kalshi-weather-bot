# Range-Scalp Bot

*Updated Fri Nov 20 09:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66152 | 57732 | 8420 (125) | 2 | $-17816.51 | -4.3% |
| **+10¢** | 49396 | 39548 | 9848 (167) | 2 | $-16616.82 | -5.4% |
| **+15¢** | 41427 | 30804 | 10623 (214) | 2 | $-14982.62 | -5.8% |
| **+20¢** | 36881 | 25723 | 11158 (270) | 2 | $-13295.91 | -5.7% |
| **+10¢ (15¢ stop)** | 80584 | 80420 | 164 (98) | 2 | $-29773.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 09:00 | +10 stop | BNB | UP | 0.62 | open |  |
| 11-20 09:00 | +20 | BNB | UP | 0.62 | open |  |
| 11-20 09:00 | +15 | BNB | UP | 0.62 | open |  |
| 11-20 09:00 | +10 | BNB | UP | 0.63 | open |  |
| 11-20 09:00 | +5 | BNB | UP | 0.63 | open |  |
| 11-20 09:00 | +10 stop | ZEC | DOWN | 0.55 | open |  |
| 11-20 09:00 | +20 | ZEC | DOWN | 0.55 | open |  |
| 11-20 09:00 | +15 | ZEC | DOWN | 0.55 | open |  |
| 11-20 09:00 | +10 | ZEC | DOWN | 0.56 | open |  |
| 11-20 09:00 | +5 | ZEC | DOWN | 0.56 | open |  |
| 11-20 08:53 | +10 stop | ZEC | DOWN | 0.48 | 0.58 | 0.64 |
| 11-20 08:52 | +10 stop | SOL | DOWN | 0.65 | 0.83 | 1.54 |
| 11-20 08:51 | +5 | SOL | DOWN | 0.59 | 0.83 | 2.13 |
| 11-20 08:51 | +10 stop | ZEC | UP | 0.65 | 0.45 | -2.34 |
| 11-20 08:51 | +5 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-20 08:50 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 08:48 | +10 stop | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-20 08:46 | +10 stop | ZEC | DOWN | 0.55 | 0.36 | -2.25 |
| 11-20 08:46 | +20 | ZEC | DOWN | 0.55 | 0.78 | 1.99 |
| 11-20 08:46 | +15 | ZEC | DOWN | 0.55 | 0.74 | 1.58 |
| 11-20 08:46 | +10 | ZEC | DOWN | 0.54 | 0.74 | 1.68 |
| 11-20 08:46 | +5 | ZEC | DOWN | 0.56 | 0.74 | 1.48 |
| 11-20 08:46 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 11-20 08:46 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-20 08:46 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-20 08:46 | +10 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 11-20 08:46 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 11-20 08:46 | +10 stop | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-20 08:46 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.93 |
| 11-20 08:46 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-20 08:46 | +10 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
| 11-20 08:46 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-20 08:46 | +10 stop | ETH | DOWN | 0.71 | 0.54 | -2.03 |
| 11-20 08:46 | +20 | ETH | DOWN | 0.71 | 0.91 | 1.79 |
| 11-20 08:46 | +15 | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-20 08:46 | +10 | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-20 08:46 | +5 | ETH | DOWN | 0.71 | 0.88 | 1.47 |
| 11-20 08:45 | +10 stop | SOL | DOWN | 0.66 | 0.46 | -2.34 |
| 11-20 08:45 | +20 | SOL | DOWN | 0.67 | 0.88 | 1.86 |
| 11-20 08:45 | +15 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
