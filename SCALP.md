# Range-Scalp Bot

*Updated Sun Nov 22 00:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68009 | 59358 | 8651 (138) | 5 | $-18202.83 | -4.3% |
| **+10¢** | 50778 | 40672 | 10106 (181) | 5 | $-16871.37 | -5.3% |
| **+15¢** | 42566 | 31670 | 10896 (230) | 7 | $-15140.41 | -5.7% |
| **+20¢** | 37891 | 26439 | 11452 (288) | 8 | $-13467.85 | -5.7% |
| **+10¢ (15¢ stop)** | 82796 | 82618 | 178 (110) | 4 | $-30403.94 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 00:37 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-22 00:37 | +10 stop | SOL | UP | 0.70 | open |  |
| 11-22 00:37 | +10 stop | HYPE | UP | 0.67 | open |  |
| 11-22 00:36 | +10 stop | NEAR | DOWN | 0.58 | 0.39 | -2.25 |
| 11-22 00:35 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-22 00:35 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 11-22 00:35 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-22 00:34 | +10 stop | NEAR | DOWN | 0.46 | 0.57 | 0.74 |
| 11-22 00:33 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-22 00:33 | +15 | HYPE | DOWN | 0.67 | open |  |
| 11-22 00:33 | +10 | HYPE | DOWN | 0.67 | open |  |
| 11-22 00:33 | +5 | HYPE | DOWN | 0.67 | open |  |
| 11-22 00:33 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.39 |
| 11-22 00:33 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-22 00:33 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-22 00:33 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-22 00:32 | +10 stop | HYPE | DOWN | 0.71 | 0.53 | -2.13 |
| 11-22 00:32 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-22 00:32 | +10 stop | NEAR | DOWN | 0.70 | 0.55 | -1.83 |
| 11-22 00:32 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-22 00:32 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-22 00:32 | +5 | NEAR | DOWN | 0.67 | open |  |
| 11-22 00:32 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-22 00:32 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-22 00:32 | +15 | BTC | DOWN | 0.67 | open |  |
| 11-22 00:32 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-22 00:32 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 11-22 00:32 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 11-22 00:32 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-22 00:32 | +15 | SOL | DOWN | 0.61 | open |  |
| 11-22 00:32 | +10 | SOL | DOWN | 0.61 | open |  |
| 11-22 00:32 | +5 | SOL | DOWN | 0.61 | 0.70 | 0.58 |
| 11-22 00:32 | +10 | DOGE | DOWN | 0.63 | 0.77 | 1.10 |
| 11-22 00:32 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-22 00:31 | +10 stop | ZEC | DOWN | 0.56 | 0.39 | -2.05 |
| 11-22 00:31 | +20 | ZEC | DOWN | 0.56 | open |  |
| 11-22 00:31 | +15 | ZEC | DOWN | 0.56 | open |  |
| 11-22 00:31 | +10 | ZEC | DOWN | 0.56 | open |  |
| 11-22 00:31 | +5 | ZEC | DOWN | 0.56 | 0.63 | 0.35 |
| 11-22 00:31 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
