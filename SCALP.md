# Range-Scalp Bot

*Updated Fri Nov 27 05:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73396 | 64052 | 9344 (165) | 4 | $-19574.41 | -4.2% |
| **+10¢** | 54698 | 43787 | 10911 (210) | 5 | $-18200.14 | -5.3% |
| **+15¢** | 45806 | 34052 | 11754 (268) | 6 | $-16314.28 | -5.7% |
| **+20¢** | 40764 | 28388 | 12376 (334) | 7 | $-14713.69 | -5.8% |
| **+10¢ (15¢ stop)** | 89401 | 89189 | 212 (129) | 3 | $-33052.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 05:52 | +10 stop | BTC | DOWN | 0.57 | open |  |
| 11-27 05:51 | +10 stop | BNB | UP | 0.54 | 0.37 | -2.05 |
| 11-27 05:51 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-27 05:50 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 11-27 05:50 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-27 05:50 | +5 | HYPE | DOWN | 0.64 | open |  |
| 11-27 05:50 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 11-27 05:50 | +10 stop | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 11-27 05:50 | +20 | SOL | DOWN | 0.57 | open |  |
| 11-27 05:50 | +15 | SOL | DOWN | 0.57 | open |  |
| 11-27 05:50 | +10 | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 11-27 05:50 | +5 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-27 05:49 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-27 05:48 | +5 | BTC | UP | 0.58 | open |  |
| 11-27 05:48 | +5 | BNB | UP | 0.52 | 0.59 | 0.35 |
| 11-27 05:48 | +5 | XRP | UP | 0.71 | 0.78 | 0.42 |
| 11-27 05:47 | +5 | DOGE | UP | 0.65 | open |  |
| 11-27 05:47 | +10 stop | NEAR | DOWN | 0.57 | 0.31 | -2.93 |
| 11-27 05:47 | +20 | NEAR | DOWN | 0.58 | open |  |
| 11-27 05:47 | +15 | NEAR | DOWN | 0.58 | open |  |
| 11-27 05:47 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-27 05:47 | +5 | NEAR | DOWN | 0.58 | 0.63 | 0.15 |
| 11-27 05:47 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-27 05:47 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-27 05:47 | +15 | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 11-27 05:47 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-27 05:47 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 11-27 05:47 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-27 05:47 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-27 05:47 | +15 | HYPE | DOWN | 0.61 | open |  |
| 11-27 05:47 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-27 05:47 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-27 05:46 | +5 | DOGE | UP | 0.54 | 0.61 | 0.35 |
| 11-27 05:46 | +10 stop | BNB | UP | 0.55 | 0.40 | -1.85 |
| 11-27 05:46 | +20 | BNB | UP | 0.55 | open |  |
| 11-27 05:46 | +15 | BNB | UP | 0.55 | open |  |
| 11-27 05:46 | +10 | BNB | UP | 0.55 | open |  |
| 11-27 05:46 | +5 | BNB | UP | 0.55 | 0.61 | 0.25 |
| 11-27 05:46 | +10 stop | BTC | UP | 0.64 | 0.49 | -1.85 |
| 11-27 05:46 | +20 | BTC | UP | 0.64 | open |  |
