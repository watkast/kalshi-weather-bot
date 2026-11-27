# Range-Scalp Bot

*Updated Fri Nov 27 06:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73476 | 64122 | 9354 (165) | 7 | $-19595.09 | -4.2% |
| **+10¢** | 54753 | 43830 | 10923 (210) | 8 | $-18225.71 | -5.3% |
| **+15¢** | 45852 | 34086 | 11766 (268) | 8 | $-16331.21 | -5.7% |
| **+20¢** | 40806 | 28417 | 12389 (334) | 8 | $-14732.89 | -5.8% |
| **+10¢ (15¢ stop)** | 89497 | 89285 | 212 (129) | 5 | $-33122.66 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 06:53 | +10 stop | XRP | DOWN | 0.57 | open |  |
| 11-27 06:53 | +10 | XRP | DOWN | 0.57 | open |  |
| 11-27 06:53 | +5 | XRP | DOWN | 0.57 | open |  |
| 11-27 06:53 | +10 stop | BNB | UP | 0.53 | open |  |
| 11-27 06:52 | +10 stop | DOGE | UP | 0.51 | open |  |
| 11-27 06:52 | +15 | DOGE | UP | 0.51 | open |  |
| 11-27 06:52 | +10 | DOGE | UP | 0.51 | open |  |
| 11-27 06:52 | +5 | DOGE | UP | 0.51 | open |  |
| 11-27 06:52 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-27 06:51 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.85 |
| 11-27 06:51 | +10 stop | ETH | UP | 0.59 | open |  |
| 11-27 06:51 | +10 stop | BTC | DOWN | 0.48 | 0.62 | 1.05 |
| 11-27 06:50 | +10 stop | BNB | DOWN | 0.60 | 0.35 | -2.83 |
| 11-27 06:50 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-27 06:50 | +20 | XRP | UP | 0.71 | open |  |
| 11-27 06:50 | +15 | XRP | UP | 0.71 | open |  |
| 11-27 06:50 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-27 06:50 | +5 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-27 06:50 | +5 | DOGE | UP | 0.56 | 0.70 | 1.07 |
| 11-27 06:49 | +10 stop | HYPE | UP | 0.59 | 0.84 | 2.23 |
| 11-27 06:49 | +5 | DOGE | UP | 0.53 | 0.63 | 0.69 |
| 11-27 06:48 | +5 | DOGE | UP | 0.52 | 0.59 | 0.35 |
| 11-27 06:48 | +10 stop | BNB | UP | 0.62 | 0.39 | -2.64 |
| 11-27 06:48 | +10 stop | ETH | UP | 0.64 | 0.49 | -1.85 |
| 11-27 06:48 | +10 stop | NEAR | DOWN | 0.59 | 0.42 | -2.05 |
| 11-27 06:48 | +10 | NEAR | DOWN | 0.58 | open |  |
| 11-27 06:47 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-27 06:46 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-27 06:46 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-27 06:46 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-27 06:46 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-27 06:46 | +5 | NEAR | DOWN | 0.61 | 0.66 | 0.17 |
| 11-27 06:46 | +10 stop | DOGE | UP | 0.57 | 0.70 | 0.97 |
| 11-27 06:46 | +20 | DOGE | UP | 0.57 | open |  |
| 11-27 06:46 | +15 | DOGE | UP | 0.56 | 0.72 | 1.28 |
| 11-27 06:46 | +10 | DOGE | UP | 0.56 | 0.70 | 1.08 |
| 11-27 06:46 | +5 | DOGE | UP | 0.56 | 0.61 | 0.16 |
| 11-27 06:46 | +10 stop | BTC | UP | 0.61 | 0.41 | -2.34 |
| 11-27 06:46 | +20 | BTC | UP | 0.61 | open |  |
| 11-27 06:46 | +15 | BTC | UP | 0.61 | open |  |
