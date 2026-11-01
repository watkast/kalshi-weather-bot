# Range-Scalp Bot

*Updated Sun Nov 01 07:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43324 | 37761 | 5563 (63) | 5 | $-12327.38 | -4.5% |
| **+10¢** | 32310 | 25885 | 6425 (85) | 5 | $-11023.43 | -5.4% |
| **+15¢** | 27036 | 20113 | 6923 (112) | 5 | $-10089.72 | -5.9% |
| **+20¢** | 24012 | 16760 | 7252 (146) | 5 | $-8895.97 | -5.9% |
| **+10¢ (15¢ stop)** | 52830 | 52745 | 85 (50) | 0 | $-19947.43 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 07:41 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 11-01 07:41 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-01 07:41 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 11-01 07:41 | +10 stop | NEAR | DOWN | 0.51 | 0.36 | -1.85 |
| 11-01 07:40 | +10 stop | SOL | UP | 0.53 | 0.34 | -2.24 |
| 11-01 07:40 | +10 stop | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-01 07:40 | +10 stop | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 11-01 07:40 | +10 stop | NEAR | UP | 0.71 | 0.48 | -2.63 |
| 11-01 07:40 | +20 | NEAR | UP | 0.71 | open |  |
| 11-01 07:40 | +15 | NEAR | UP | 0.71 | open |  |
| 11-01 07:40 | +10 | NEAR | UP | 0.71 | open |  |
| 11-01 07:40 | +5 | NEAR | UP | 0.71 | open |  |
| 11-01 07:39 | +10 stop | ETH | UP | 0.49 | 0.62 | 0.95 |
| 11-01 07:38 | +10 stop | SOL | UP | 0.66 | 0.51 | -1.84 |
| 11-01 07:37 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-01 07:36 | +5 | BTC | UP | 0.67 | open |  |
| 11-01 07:35 | +10 stop | SOL | UP | 0.59 | 0.76 | 1.40 |
| 11-01 07:35 | +10 stop | ETH | UP | 0.54 | 0.65 | 0.76 |
| 11-01 07:35 | +10 stop | BTC | UP | 0.59 | 0.38 | -2.44 |
| 11-01 07:34 | +10 stop | ZEC | DOWN | 0.67 | 0.51 | -1.94 |
| 11-01 07:34 | +10 | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-01 07:34 | +5 | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 11-01 07:33 | +10 stop | BTC | DOWN | 0.56 | 0.41 | -1.85 |
| 11-01 07:33 | +10 stop | SOL | DOWN | 0.59 | 0.40 | -2.24 |
| 11-01 07:33 | +20 | SOL | DOWN | 0.59 | open |  |
| 11-01 07:33 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-01 07:33 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-01 07:33 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-01 07:33 | +10 stop | ETH | DOWN | 0.67 | 0.45 | -2.54 |
| 11-01 07:33 | +20 | ETH | DOWN | 0.67 | open |  |
| 11-01 07:33 | +15 | ETH | DOWN | 0.67 | open |  |
| 11-01 07:33 | +10 | ETH | DOWN | 0.67 | open |  |
| 11-01 07:33 | +5 | ETH | DOWN | 0.67 | open |  |
| 11-01 07:33 | +10 stop | XRP | UP | 0.62 | 0.80 | 1.51 |
| 11-01 07:33 | +10 | XRP | UP | 0.62 | 0.80 | 1.51 |
| 11-01 07:33 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-01 07:33 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-01 07:32 | +10 stop | NEAR | UP | 0.53 | 0.74 | 1.78 |
| 11-01 07:32 | +20 | NEAR | UP | 0.55 | 0.75 | 1.68 |
| 11-01 07:32 | +15 | NEAR | UP | 0.55 | 0.74 | 1.58 |
