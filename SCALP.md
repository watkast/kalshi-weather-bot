# Range-Scalp Bot

*Updated Sun Oct 11 11:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11847 | 10221 | 1626 (24) | 3 | $-3960.99 | -5.3% |
| **+10¢** | 8982 | 7090 | 1892 (37) | 4 | $-3781.08 | -6.7% |
| **+15¢** | 7567 | 5559 | 2008 (54) | 3 | $-3235.04 | -6.8% |
| **+20¢** | 6742 | 4655 | 2087 (67) | 3 | $-2708.94 | -6.4% |
| **+10¢ (15¢ stop)** | 14576 | 14535 | 41 (25) | 1 | $-5767.78 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 11:12 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 10-11 11:11 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-11 11:11 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-11 11:11 | +20 | XRP | DOWN | 0.61 | 0.88 | 2.45 |
| 10-11 11:11 | +15 | XRP | DOWN | 0.61 | 0.80 | 1.61 |
| 10-11 11:11 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-11 11:11 | +5 | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-11 11:10 | +10 stop | BNB | UP | 0.66 | open |  |
| 10-11 11:09 | +10 stop | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-11 11:09 | +20 | DOGE | DOWN | 0.57 | 0.78 | 1.79 |
| 10-11 11:09 | +15 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-11 11:09 | +10 | DOGE | DOWN | 0.57 | 0.73 | 1.28 |
| 10-11 11:09 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
| 10-11 11:09 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.85 |
| 10-11 11:09 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-11 11:09 | +15 | SOL | DOWN | 0.59 | 0.77 | 1.49 |
| 10-11 11:09 | +10 | SOL | DOWN | 0.59 | 0.71 | 0.87 |
| 10-11 11:09 | +5 | SOL | DOWN | 0.59 | 0.68 | 0.57 |
| 10-11 11:09 | +10 stop | ETH | UP | 0.67 | 0.48 | -2.24 |
| 10-11 11:09 | +20 | ETH | UP | 0.67 | open |  |
| 10-11 11:09 | +15 | ETH | UP | 0.67 | open |  |
| 10-11 11:09 | +10 | ETH | UP | 0.67 | open |  |
| 10-11 11:09 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 10-11 11:05 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 10-11 11:05 | +15 | ZEC | DOWN | 0.64 | 0.81 | 1.42 |
| 10-11 11:05 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-11 11:05 | +15 | ETH | UP | 0.66 | 0.85 | 1.65 |
| 10-11 11:05 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-11 11:05 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 10-11 11:04 | +10 stop | ZEC | UP | 0.55 | 0.36 | -2.25 |
| 10-11 11:04 | +10 | ZEC | UP | 0.55 | open |  |
| 10-11 11:04 | +5 | ZEC | UP | 0.55 | open |  |
| 10-11 11:03 | +10 stop | HYPE | UP | 0.70 | 0.82 | 0.94 |
| 10-11 11:03 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-11 11:03 | +10 stop | ZEC | DOWN | 0.45 | 0.57 | 0.84 |
| 10-11 11:03 | +15 | ZEC | DOWN | 0.45 | 0.62 | 1.35 |
| 10-11 11:03 | +10 | ZEC | DOWN | 0.46 | 0.57 | 0.74 |
| 10-11 11:03 | +5 | ZEC | DOWN | 0.44 | 0.57 | 0.94 |
| 10-11 11:02 | +10 stop | XRP | UP | 0.63 | 0.75 | 0.89 |
| 10-11 11:02 | +20 | XRP | UP | 0.63 | 0.83 | 1.73 |
