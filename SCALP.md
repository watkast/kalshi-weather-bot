# Range-Scalp Bot

*Updated Sun Oct 25 13:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33212 | 28982 | 4230 (42) | 3 | $-9292.50 | -4.4% |
| **+10¢** | 24861 | 19964 | 4897 (60) | 2 | $-8255.93 | -5.3% |
| **+15¢** | 20802 | 15529 | 5273 (83) | 3 | $-7433.18 | -5.7% |
| **+20¢** | 18432 | 12910 | 5522 (105) | 3 | $-6549.17 | -5.7% |
| **+10¢ (15¢ stop)** | 40742 | 40682 | 60 (32) | 0 | $-15550.53 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 13:35 | +10 stop | BTC | UP | 0.50 | 0.60 | 0.65 |
| 10-25 13:35 | +10 stop | ETH | UP | 0.48 | 0.74 | 2.28 |
| 10-25 13:34 | +10 stop | NEAR | UP | 0.58 | 0.75 | 1.37 |
| 10-25 13:34 | +10 stop | DOGE | UP | 0.58 | 0.72 | 1.07 |
| 10-25 13:34 | +10 stop | HYPE | DOWN | 0.60 | 0.74 | 1.09 |
| 10-25 13:34 | +5 | XRP | UP | 0.71 | 0.79 | 0.53 |
| 10-25 13:34 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-25 13:34 | +10 stop | SOL | DOWN | 0.49 | 0.28 | -2.43 |
| 10-25 13:34 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-25 13:33 | +10 stop | ETH | DOWN | 0.70 | 0.53 | -2.03 |
| 10-25 13:33 | +20 | ETH | DOWN | 0.70 | open |  |
| 10-25 13:33 | +15 | ETH | DOWN | 0.70 | open |  |
| 10-25 13:33 | +10 | ETH | DOWN | 0.70 | open |  |
| 10-25 13:33 | +5 | ETH | DOWN | 0.70 | open |  |
| 10-25 13:33 | +10 stop | BNB | UP | 0.60 | 0.81 | 1.82 |
| 10-25 13:33 | +5 | ZEC | UP | 0.70 | 0.75 | 0.21 |
| 10-25 13:33 | +10 stop | SOL | UP | 0.60 | 0.42 | -2.15 |
| 10-25 13:33 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 10-25 13:33 | +10 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-25 13:33 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 10-25 13:32 | +10 stop | DOGE | UP | 0.68 | 0.47 | -2.42 |
| 10-25 13:32 | +20 | DOGE | UP | 0.68 | 0.88 | 1.78 |
| 10-25 13:32 | +15 | DOGE | UP | 0.68 | 0.84 | 1.36 |
| 10-25 13:32 | +10 | DOGE | UP | 0.68 | 0.84 | 1.36 |
| 10-25 13:32 | +5 | DOGE | UP | 0.68 | 0.84 | 1.37 |
| 10-25 13:32 | +10 stop | HYPE | UP | 0.55 | 0.35 | -2.34 |
| 10-25 13:32 | +20 | HYPE | UP | 0.55 | 0.84 | 2.62 |
| 10-25 13:32 | +15 | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 10-25 13:32 | +10 | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 10-25 13:32 | +5 | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 10-25 13:31 | +10 stop | NEAR | UP | 0.70 | 0.51 | -2.23 |
| 10-25 13:31 | +20 | NEAR | UP | 0.70 | open |  |
| 10-25 13:31 | +15 | NEAR | UP | 0.70 | open |  |
| 10-25 13:31 | +10 | NEAR | UP | 0.70 | 0.83 | 1.03 |
| 10-25 13:31 | +5 | NEAR | UP | 0.70 | 0.80 | 0.71 |
| 10-25 13:31 | +10 stop | SOL | UP | 0.56 | 0.72 | 1.27 |
| 10-25 13:31 | +20 | SOL | UP | 0.56 | 0.77 | 1.79 |
| 10-25 13:31 | +15 | SOL | UP | 0.55 | 0.72 | 1.37 |
| 10-25 13:31 | +10 | SOL | UP | 0.55 | 0.72 | 1.37 |
| 10-25 13:31 | +5 | SOL | UP | 0.55 | 0.63 | 0.45 |
