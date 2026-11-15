# Range-Scalp Bot

*Updated Sun Nov 15 03:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60296 | 52589 | 7707 (107) | 6 | $-16456.14 | -4.3% |
| **+10¢** | 45058 | 36027 | 9031 (143) | 6 | $-15545.82 | -5.5% |
| **+15¢** | 37747 | 28008 | 9739 (181) | 6 | $-14210.40 | -6.0% |
| **+20¢** | 33643 | 23425 | 10218 (233) | 6 | $-12532.30 | -5.9% |
| **+10¢ (15¢ stop)** | 73428 | 73285 | 143 (82) | 1 | $-27037.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 03:53 | +10 stop | HYPE | UP | 0.59 | open |  |
| 11-15 03:52 | +5 | HYPE | UP | 0.71 | open |  |
| 11-15 03:49 | +5 | HYPE | UP | 0.64 | 0.76 | 0.91 |
| 11-15 03:49 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-15 03:48 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-15 03:48 | +10 stop | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-15 03:48 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-15 03:48 | +20 | BTC | DOWN | 0.64 | 0.88 | 2.15 |
| 11-15 03:48 | +15 | BTC | DOWN | 0.63 | 0.88 | 2.25 |
| 11-15 03:48 | +10 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-15 03:48 | +5 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-15 03:48 | +10 stop | SOL | DOWN | 0.71 | 0.85 | 1.20 |
| 11-15 03:48 | +20 | SOL | DOWN | 0.71 | 0.93 | 2.03 |
| 11-15 03:48 | +15 | SOL | DOWN | 0.70 | 0.86 | 1.33 |
| 11-15 03:48 | +10 | SOL | DOWN | 0.70 | 0.85 | 1.22 |
| 11-15 03:48 | +5 | SOL | DOWN | 0.70 | 0.78 | 0.52 |
| 11-15 03:47 | +10 stop | BNB | UP | 0.53 | 0.31 | -2.53 |
| 11-15 03:47 | +20 | BNB | UP | 0.53 | open |  |
| 11-15 03:47 | +15 | BNB | UP | 0.53 | open |  |
| 11-15 03:47 | +10 | BNB | UP | 0.53 | open |  |
| 11-15 03:47 | +5 | BNB | UP | 0.53 | open |  |
| 11-15 03:47 | +10 stop | XRP | DOWN | 0.58 | 0.70 | 0.87 |
| 11-15 03:46 | +10 stop | HYPE | UP | 0.71 | 0.55 | -1.93 |
| 11-15 03:46 | +20 | HYPE | UP | 0.71 | open |  |
| 11-15 03:46 | +15 | HYPE | UP | 0.71 | open |  |
| 11-15 03:46 | +10 | HYPE | UP | 0.71 | open |  |
| 11-15 03:46 | +5 | HYPE | UP | 0.71 | 0.77 | 0.32 |
| 11-15 03:46 | +10 stop | ZEC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-15 03:46 | +20 | ZEC | DOWN | 0.56 | 0.80 | 2.10 |
| 11-15 03:46 | +15 | ZEC | DOWN | 0.56 | 0.71 | 1.17 |
| 11-15 03:46 | +10 | ZEC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-15 03:46 | +5 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 03:45 | +10 stop | NEAR | UP | 0.58 | 0.43 | -1.86 |
| 11-15 03:45 | +20 | NEAR | UP | 0.58 | open |  |
| 11-15 03:45 | +15 | NEAR | UP | 0.58 | open |  |
| 11-15 03:45 | +10 | NEAR | UP | 0.58 | open |  |
| 11-15 03:45 | +5 | NEAR | UP | 0.58 | open |  |
| 11-15 03:45 | +10 stop | ETH | UP | 0.53 | 0.35 | -2.14 |
| 11-15 03:45 | +20 | ETH | UP | 0.54 | open |  |
| 11-15 03:45 | +15 | ETH | UP | 0.54 | open |  |
