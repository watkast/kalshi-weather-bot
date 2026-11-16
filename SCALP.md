# Range-Scalp Bot

*Updated Mon Nov 16 07:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61722 | 53858 | 7864 (115) | 5 | $-16617.49 | -4.3% |
| **+10¢** | 46108 | 36895 | 9213 (157) | 5 | $-15547.86 | -5.4% |
| **+15¢** | 38635 | 28696 | 9939 (196) | 6 | $-14182.18 | -5.9% |
| **+20¢** | 34443 | 24019 | 10424 (249) | 6 | $-12393.72 | -5.7% |
| **+10¢ (15¢ stop)** | 75117 | 74963 | 154 (90) | 0 | $-27651.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 07:33 | +10 stop | ETH | UP | 0.70 | 0.81 | 0.84 |
| 11-16 07:33 | +10 stop | XRP | UP | 0.65 | 0.77 | 0.91 |
| 11-16 07:33 | +10 stop | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 11-16 07:33 | +20 | HYPE | UP | 0.68 | 0.94 | 2.38 |
| 11-16 07:33 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 11-16 07:33 | +10 | HYPE | UP | 0.68 | 0.78 | 0.71 |
| 11-16 07:33 | +5 | HYPE | UP | 0.69 | 0.74 | 0.21 |
| 11-16 07:31 | +10 stop | ZEC | UP | 0.64 | 0.79 | 1.21 |
| 11-16 07:31 | +20 | ZEC | UP | 0.64 | 0.84 | 1.73 |
| 11-16 07:31 | +15 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-16 07:31 | +10 | ZEC | UP | 0.62 | 0.79 | 1.41 |
| 11-16 07:31 | +5 | ZEC | UP | 0.62 | 0.69 | 0.38 |
| 11-16 07:31 | +10 stop | SOL | DOWN | 0.60 | 0.36 | -2.74 |
| 11-16 07:31 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-16 07:31 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-16 07:31 | +10 stop | NEAR | DOWN | 0.62 | 0.21 | -4.39 |
| 11-16 07:31 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-16 07:31 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-16 07:31 | +10 | NEAR | DOWN | 0.62 | open |  |
| 11-16 07:31 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-16 07:31 | +10 stop | ETH | DOWN | 0.55 | 0.31 | -2.73 |
| 11-16 07:31 | +20 | ETH | DOWN | 0.57 | open |  |
| 11-16 07:31 | +15 | ETH | DOWN | 0.57 | open |  |
| 11-16 07:31 | +10 | ETH | DOWN | 0.57 | open |  |
| 11-16 07:31 | +5 | ETH | DOWN | 0.57 | open |  |
| 11-16 07:31 | +10 stop | XRP | DOWN | 0.60 | 0.41 | -2.24 |
| 11-16 07:31 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-16 07:31 | +15 | XRP | DOWN | 0.60 | open |  |
| 11-16 07:31 | +10 | XRP | DOWN | 0.60 | open |  |
| 11-16 07:31 | +5 | XRP | DOWN | 0.60 | open |  |
| 11-16 07:31 | +10 stop | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-16 07:31 | +20 | DOGE | DOWN | 0.53 | open |  |
| 11-16 07:31 | +15 | DOGE | DOWN | 0.53 | open |  |
| 11-16 07:31 | +10 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-16 07:31 | +5 | DOGE | DOWN | 0.53 | 0.63 | 0.65 |
| 11-16 07:31 | +10 stop | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 11-16 07:31 | +20 | SOL | DOWN | 0.52 | open |  |
| 11-16 07:31 | +15 | SOL | DOWN | 0.52 | open |  |
| 11-16 07:31 | +10 | SOL | DOWN | 0.52 | 0.66 | 1.06 |
| 11-16 07:31 | +5 | SOL | DOWN | 0.52 | 0.66 | 1.06 |
