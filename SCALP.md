# Range-Scalp Bot

*Updated Sat Oct 17 01:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20193 | 17561 | 2632 (29) | 2 | $-5989.21 | -4.7% |
| **+10¢** | 15211 | 12172 | 3039 (41) | 4 | $-5363.05 | -5.6% |
| **+15¢** | 12717 | 9446 | 3271 (60) | 6 | $-4868.42 | -6.1% |
| **+20¢** | 11276 | 7849 | 3427 (79) | 5 | $-4329.36 | -6.1% |
| **+10¢ (15¢ stop)** | 24833 | 24783 | 50 (29) | 1 | $-9427.63 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 01:38 | +10 stop | HYPE | DOWN | 0.71 | open |  |
| 10-17 01:37 | +10 stop | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 01:37 | +20 | XRP | DOWN | 0.64 | 0.87 | 2.05 |
| 10-17 01:37 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 01:37 | +10 | XRP | DOWN | 0.64 | 0.81 | 1.44 |
| 10-17 01:37 | +5 | XRP | DOWN | 0.58 | 0.63 | 0.15 |
| 10-17 01:36 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 10-17 01:36 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-17 01:36 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-17 01:36 | +5 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-17 01:36 | +10 stop | HYPE | DOWN | 0.63 | 0.45 | -2.15 |
| 10-17 01:36 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-17 01:36 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-17 01:36 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-17 01:36 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-17 01:36 | +15 | BTC | DOWN | 0.69 | open |  |
| 10-17 01:36 | +10 | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-17 01:36 | +10 stop | ETH | DOWN | 0.70 | 0.88 | 1.57 |
| 10-17 01:36 | +5 | ETH | DOWN | 0.70 | 0.88 | 1.59 |
| 10-17 01:34 | +10 stop | NEAR | DOWN | 0.69 | 0.50 | -2.22 |
| 10-17 01:34 | +10 stop | BNB | DOWN | 0.61 | 0.44 | -2.05 |
| 10-17 01:33 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-17 01:33 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-17 01:33 | +10 stop | NEAR | UP | 0.65 | 0.50 | -1.84 |
| 10-17 01:33 | +10 | NEAR | UP | 0.68 | open |  |
| 10-17 01:33 | +5 | NEAR | UP | 0.66 | open |  |
| 10-17 01:33 | +10 stop | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-17 01:33 | +10 | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-17 01:33 | +5 | ZEC | UP | 0.55 | 0.66 | 0.76 |
| 10-17 01:33 | +10 stop | SOL | UP | 0.41 | 0.57 | 1.25 |
| 10-17 01:33 | +10 stop | XRP | UP | 0.42 | 0.59 | 1.35 |
| 10-17 01:32 | +10 stop | ETH | UP | 0.59 | 0.36 | -2.64 |
| 10-17 01:32 | +20 | ETH | UP | 0.59 | open |  |
| 10-17 01:32 | +15 | ETH | UP | 0.59 | open |  |
| 10-17 01:32 | +10 | ETH | UP | 0.59 | open |  |
| 10-17 01:32 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 10-17 01:32 | +10 stop | BNB | UP | 0.59 | 0.44 | -1.85 |
| 10-17 01:32 | +10 stop | ZEC | UP | 0.57 | 0.67 | 0.66 |
| 10-17 01:32 | +20 | ZEC | UP | 0.57 | open |  |
| 10-17 01:32 | +15 | ZEC | UP | 0.57 | open |  |
