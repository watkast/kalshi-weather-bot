# Range-Scalp Bot

*Updated Wed Oct 14 00:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15185 | 13137 | 2048 (27) | 0 | $-4905.95 | -5.1% |
| **+10¢** | 11483 | 9106 | 2377 (39) | 0 | $-4588.84 | -6.3% |
| **+15¢** | 9648 | 7105 | 2543 (58) | 2 | $-4075.30 | -6.7% |
| **+20¢** | 8580 | 5924 | 2656 (74) | 2 | $-3563.66 | -6.6% |
| **+10¢ (15¢ stop)** | 18612 | 18562 | 50 (29) | 0 | $-7174.60 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 00:17 | +10 stop | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-14 00:17 | +10 | BNB | UP | 0.71 | 0.82 | 0.84 |
| 10-14 00:17 | +5 | BNB | UP | 0.71 | 0.79 | 0.53 |
| 10-14 00:17 | +10 stop | BNB | DOWN | 0.42 | 0.55 | 0.94 |
| 10-14 00:17 | +20 | BNB | DOWN | 0.42 | open |  |
| 10-14 00:17 | +15 | BNB | DOWN | 0.42 | open |  |
| 10-14 00:17 | +10 | BNB | DOWN | 0.42 | 0.55 | 0.94 |
| 10-14 00:17 | +5 | BNB | DOWN | 0.42 | 0.55 | 0.94 |
| 10-14 00:17 | +10 stop | NEAR | DOWN | 0.44 | 0.54 | 0.64 |
| 10-14 00:17 | +20 | NEAR | DOWN | 0.44 | open |  |
| 10-14 00:17 | +15 | NEAR | DOWN | 0.43 | open |  |
| 10-14 00:17 | +10 | NEAR | DOWN | 0.43 | 0.54 | 0.74 |
| 10-14 00:17 | +5 | NEAR | DOWN | 0.43 | 0.54 | 0.74 |
| 10-14 00:17 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-14 00:17 | +20 | HYPE | UP | 0.65 | 0.85 | 1.75 |
| 10-14 00:17 | +15 | HYPE | UP | 0.66 | 0.82 | 1.33 |
| 10-14 00:17 | +10 | HYPE | UP | 0.66 | 0.78 | 0.91 |
| 10-14 00:17 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 10-14 00:16 | +10 stop | ZEC | UP | 0.61 | 0.78 | 1.40 |
| 10-14 00:16 | +20 | ZEC | UP | 0.61 | 0.82 | 1.82 |
| 10-14 00:16 | +15 | ZEC | UP | 0.61 | 0.78 | 1.40 |
| 10-14 00:16 | +10 | ZEC | UP | 0.61 | 0.78 | 1.40 |
| 10-14 00:16 | +5 | ZEC | UP | 0.61 | 0.78 | 1.40 |
| 10-14 00:16 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.10 |
| 10-14 00:16 | +20 | SOL | UP | 0.60 | 0.83 | 2.06 |
| 10-14 00:16 | +15 | SOL | UP | 0.60 | 0.83 | 2.06 |
| 10-14 00:16 | +10 | SOL | UP | 0.60 | 0.74 | 1.12 |
| 10-14 00:16 | +5 | SOL | UP | 0.60 | 0.74 | 1.12 |
| 10-14 00:16 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-14 00:16 | +20 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-14 00:16 | +15 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-14 00:16 | +10 | ETH | UP | 0.60 | 0.72 | 0.88 |
| 10-14 00:16 | +5 | ETH | UP | 0.60 | 0.72 | 0.88 |
| 10-14 00:06 | +10 stop | NEAR | DOWN | 0.60 | 0.32 | -3.13 |
| 10-14 00:05 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-14 00:05 | +10 | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-14 00:05 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 10-14 00:04 | +10 stop | NEAR | UP | 0.68 | 0.37 | -3.43 |
| 10-14 00:04 | +10 | NEAR | UP | 0.68 | 0.79 | 0.82 |
| 10-14 00:04 | +5 | NEAR | UP | 0.68 | 0.77 | 0.61 |
